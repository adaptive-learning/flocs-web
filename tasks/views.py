from rest_framework import viewsets
from tasks.serializers import InstructionSerializer, TaskSerializer, CategorySerializer, \
                              LevelSerializer, ToolboxSerializer, BlockSerializer
from .models import Instruction, Task, Category, Level, Toolbox, Block


class InstructionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents instructions available in the system.
    """
    serializer_class = InstructionSerializer
    queryset = Instruction.objects.all()


class TaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents tasks available in the system.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents task categories available in the system.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all().prefetch_related('tasks')


class LevelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents levels available in the system.
    """
    serializer_class = LevelSerializer
    queryset = Level.objects.all()


class ToolboxViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents toolboxes available in the system.
    """
    serializer_class = ToolboxSerializer
    queryset = Toolbox.objects.all().prefetch_related('blocks')


class BlockViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents blocks available in the system.
    """
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
