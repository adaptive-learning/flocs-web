from django.conf import global_settings, settings
from django.contrib.sessions.models import Session
from django.shortcuts import redirect, render
from django.views.decorators.csrf import ensure_csrf_cookie
from json import loads
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
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
    response = render(request, 'index.html')
    # In case there is an invalid or otherwise corrupted session id cookie sent
    # from the user, delete the cookie right away. If we ignore invalid
    # session ids, it causes unpredictable problems when running parallel
    # requests from the frontend app as each response will instruct the browser
    # to set a new session id resulting in a race condition.
    if request.session.session_key and not Session.objects.filter(pk=request.session.session_key).exists():
        cookie_name = settings.SESSION_COOKIE_NAME if hasattr(settings, 'SESSION_COOKIE_NAME') \
            else global_settings.SESSION_COOKIE_NAME
        response.delete_cookie(cookie_name)
    return response


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

        # inject student
        user = self.request.user
        if hasattr(user, 'student'):
            action_data['student_id'] = user.student.student_id

        with open_django_store(request=self.request) as store:
            intent = actions.create(type=action_type, data=action_data)
            action = store.add(intent)
        # The Action is already created, but calling serializer.save() is still
        # necessary, because rest framework needs to have been passed the
        # created action somehow in order to return it to the client
        serializer.save(**action._asdict())
