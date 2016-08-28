from rest_framework import viewsets
from tasks.serializers import TaskSerializer
from .models import Task


class TasksViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents tasks available in the system.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
