from rest_framework import serializers


class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField()
    revision = serializers.IntegerField()
    maze_settings = serializers.JSONField(source='get_maze_settings')
    workspace_settings = serializers.JSONField(source='get_workspace_settings')
