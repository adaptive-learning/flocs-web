from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StudentSerializer, TaskSessionSerializer
from .models import Student, TaskSession
from .permissions import IsAdminOrOwnerPostAnyone


class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents student instances. The student is an extension of the system user.

    Regular users can only access them selves. Staff members can see all the students.
    """

    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return Student.objects.all()
        return Student.objects.filter(user=user)


class TaskSessionsViewSet(viewsets.ModelViewSet):
    """
    This view presents task session instances.

    Regular users can only access their own instances. Staff members can see all the instances.
    """

    serializer_class = TaskSessionSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return TaskSession.objects.all()
        return TaskSession.objects.filter(student__user=user)
