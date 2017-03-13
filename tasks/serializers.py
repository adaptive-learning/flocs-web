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


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'category_id', 'level', 'toolbox')


class LevelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Level
        fields = ('url', 'level_id', 'credits')


class BlockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Block
        fields = ('url', 'block_id')


class ToolboxSerializer(serializers.ModelSerializer):
    blocks = BlockSerializer(many=True)

    class Meta:
        model = Toolbox
        fields = ('url', 'toolbox_id', 'blocks')
