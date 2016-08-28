from rest_framework import serializers
from .models import Student, TaskInstance


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'student_id', 'user')


class TaskInstanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskInstance
        fields = ('url', 'task_instance_id', 'student', 'task', 'solved', 'given_up')

        extra_kwargs = {
            'url': {'view_name': 'task_instance-detail'}
        }

    def validate(self, data):
        """
        Check that the task is not solved and given up at the same time.
        """
        if data['solved'] and data['given_up']:
            raise serializers.ValidationError("A task cannot be solved and given up at the same time.")
        return data
