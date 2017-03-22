from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from json import loads
from lazysignup.decorators import allow_lazy_user
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins
from flocs import actions
from .models import Action
from .serializers import ActionSerializer
from .store import open_django_store


@api_view()
def wrong_api_call(request):
    """
    Handles non-existent API calls (404 error).
    """
    raise NotFound(detail='Wrong api call.')


def redirect_home(request):
    """
    Redirect to home path URL
    """
    return redirect('/')


@ensure_csrf_cookie
def frontend_app(request, *_):
    return render(request, 'index.html')

# TODO: move to user app
@allow_lazy_user
@api_view(['GET', 'POST'])
def get_or_create_user(request):
    """ Return a current user and creates one if not exists

    Creating a new "lazy user" is delegated to django-lazysignup library
    """
    if request.method == 'GET':
        return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
    return Response(request.user)


class ActionsViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    """ Provides views for listing actions or creating new ones
    """
    queryset = Action.objects.all()
    serializer_class = ActionSerializer

    def perform_create(self, serializer):
        """ Perform a new action in our domain model
        """
        action_type = serializer.validated_data['type']
        action_data = loads(serializer.validated_data['data'])
        if action_type == 'create-student' and hasattr(self.request.user, 'student'):
            raise ValidationError('Student already created for this user')
        with open_django_store(request=self.request) as store:
            action = actions.create(
                type=action_type,
                data=action_data)
            store.stage_action(action)
        # The Action is already created, but calling serializer.save() is still
        # necessary, because rest framework needs to have been passed the
        # created action somehow in order to return it to the client
        serializer.save(**action._asdict())
