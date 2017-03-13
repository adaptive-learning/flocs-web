from rest_framework import serializers
from .models import Student, TaskSession


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student


class TaskSessionSerializer(serializers.HyperlinkedModelSerializer):
    solve = serializers.HyperlinkedIdentityField(
        view_name='task_session-solve-task',
        read_only=True)
    give_up = serializers.HyperlinkedIdentityField(
        view_name='task_session-give-up-task',
        read_only=True)

    class Meta:
        model = TaskSession
        fields = ('url', 'task_session_id', 'student', 'task', 'solved', 'given_up', 'solve', 'give_up')

        extra_kwargs = {
            'url': {'view_name': 'task_session-detail'},
        }

    def validate(self, data):
        """
        Check that the task is not solved and given up at the same time.
        """
        if data['solved'] and data['given_up']:
            raise serializers.ValidationError("A task cannot be solved and given up at the same time.")
        return data
