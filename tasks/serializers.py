from rest_framework import serializers
from .models import Instruction, Task, Block, Category, Level, Toolbox

class InstructionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instruction
        fields = ('instruction_id',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('url', 'task_id', 'category', 'setting', 'solution')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('url', 'level_id', 'credits')


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('url', 'block_id')


class ToolboxSerializer(serializers.ModelSerializer):
    blocks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Toolbox
        fields = ('url', 'toolbox_id', 'blocks')


class CategorySerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('url', 'category_id', 'level', 'toolbox', 'tasks')
