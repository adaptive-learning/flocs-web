from rest_framework import serializers
from .models import Student, TaskSession


class TaskSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TaskSession
        fields = ('url', 'task_session_id', 'student', 'task', 'solved', 'given_up')

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


class StudentSerializer(serializers.ModelSerializer):
    task_sessions = TaskSessionSerializer(many=True)
    class Meta:
        model = Student
