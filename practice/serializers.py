from rest_framework import serializers
from .models import Student, TaskSession


class TaskSessionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TaskSession
        fields = ('url', 'task_session_id', 'student', 'task', 'solved', 'given_up',
                  'start', 'end')

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


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    practice_overview = serializers.HyperlinkedIdentityField(
        view_name='student-practice-overview',
        read_only=True)

    solve_task = serializers.HyperlinkedIdentityField(
        view_name='student-solve-task',
        read_only=True)

    class Meta:
        model = Student


class StudentInstructionSerializer(serializers.Serializer):
    instruction_id = serializers.CharField()
    seen = serializers.BooleanField()


class StudentTaskSerializer(serializers.Serializer):
    task_id = serializers.CharField()
    solved = serializers.BooleanField()
    time = serializers.DurationField()


class RecommendationSerializer(serializers.Serializer):
    available = serializers.BooleanField()
    task_id = serializers.CharField()


class PracticeOverviewSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    credits = serializers.IntegerField()
    active_credits = serializers.IntegerField()
    instructions = StudentInstructionSerializer(many=True)
    tasks = StudentTaskSerializer(many=True)
    recommendation = RecommendationSerializer()


class SolveTaskDiffSerializer(serializers.Serializer):
    level = serializers.IntegerField()
    credits = serializers.IntegerField()
    active_credits = serializers.IntegerField()
    recommendation = RecommendationSerializer()
