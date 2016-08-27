from rest_framework import viewsets
from tasks.serializers import TaskSerializer
from .models import Task


class TasksViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
