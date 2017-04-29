from uuid import UUID
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from flocs.actions import EditProgram, RunProgram, SolveTask
from flocs.extractors import get_practice_overview, get_recommendation
from flocsweb.store import open_django_store
from .serializers import StudentSerializer, TaskSessionSerializer
from .serializers import PracticeOverviewSerializer
from .serializers import SolveTaskDiffSerializer
from .models import Student, TaskSession
from .permissions import IsAdminOrOwnerPostAnyone


class StudentsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view presents student instances. The student is an extension of the system user.

    Regular users can only access them selves. Staff members can see all the students.
    """
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return Student.objects.all()
        return Student.objects.filter(user=user)

    @detail_route(methods=['get'])
    def practice_overview(self, request, pk=None):
        with open_django_store(request=request) as store:
            overview = get_practice_overview(store.state, student_id=pk)
        serializer = PracticeOverviewSerializer(overview)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def solve_task(self, request, pk=None):
        with open_django_store(request=request) as store:
            intent = SolveTask(
                task_session_id=UUID(request.data['task-session-id']))
            store.add(intent)
        # NOTE: current db store implementation doesn't allow to read
        # uncommited changes, so we need to commit and re-open the with-block
        # before computing changes... (TODO: fix it)
        with open_django_store(request=request) as store:
            diff = {
                'level': 0,
                'credits': 0,
                'active_credits': 0,
                'recommendation': get_recommendation(store.state, student_id=pk),
            }
        serializer = SolveTaskDiffSerializer(diff)
        return Response(serializer.data)

    @detail_route(methods=['post'])
    def edit_program(self, request, pk=None):
        del pk  # TODO: check that student matches request.user (?)
        with open_django_store(request=request) as store:
            intent = EditProgram(
                task_session_id=UUID(request.data['task-session-id']),
                program=request.data['program'],
            )
            store.add(intent)
        return Response()

    @detail_route(methods=['post'])
    def run_program(self, request, pk=None):
        del pk  # TODO: check that student matches request.user (?)
        with open_django_store(request=request) as store:
            intent = RunProgram(
                task_session_id=UUID(request.data['task-session-id']),
                program=request.data['program'],
                correct=request.data['correct'],
            )
            store.add(intent)
        return Response()


class TaskSessionsViewSet(viewsets.ModelViewSet):
    """
    This view presents task session instances.

    Regular users can only access their own instances. Staff members can see all the instances.
    """

    serializer_class = TaskSessionSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return TaskSession.objects.all()
        return TaskSession.objects.filter(student__user=user)
