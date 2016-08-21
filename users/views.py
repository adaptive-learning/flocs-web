from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.reverse import reverse
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .serializers import UserSerializer
from .permissions import IsAdminOrSelfPostAnyone


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrSelfPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.pk)

    @list_route()
    def current_user(self, request):
        """
        Issue redirect to details of currently logged in user.
        """
        pk = request.user.pk
        if pk:
            return redirect(reverse('user-detail', args=[pk], request=request))
        else:
            raise NotFound(detail='No user available.')
