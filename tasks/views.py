from flocsweb import viewsets
from tasks.serializers import TaskSerializer
from core.data.fixtures.tasks import TASKS


class TasksViewSet(viewsets.ReadOnlyNonModelViewSet):
    serializer_class = TaskSerializer
    fixtures = TASKS
