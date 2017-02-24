from collections import OrderedDict
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view, permission_classes
from lazysignup.decorators import allow_lazy_user
from .serializers import StudentSerializer, TaskSessionSerializer
from .models import Student, TaskSession
from .permissions import IsAdminOrOwnerPostAnyone
from flocs import actions
from flocs.extractors import select_task_fixed_then_random
from flocsweb.store import open_django_store
from tasks.models import Task


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

    @detail_route(methods=['GET', 'POST'])
    def solve_task(self, request, pk=None):
        if request.method == 'GET':
            return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
        if not self.get_object().is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="This task session is already closed.")
        with open_django_store() as store:
            action = actions.solve_task(pk)
            store.stage_action(action)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['GET', 'POST'])
    def give_up_task(self, request, pk=None):
        if request.method == 'GET':
            return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
        if not self.get_object().is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="This task session is already closed.")
        with open_django_store() as store:
            action = actions.give_up_task(pk)
            store.stage_action(action)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PracticeViewSet(viewsets.GenericViewSet):
    """
    This page does not do anything. You can perform any of the following actions.

    - get a task id of based on system's recommendation
    - practice a specific task of your choice

    In case of practicing a specific task, substitute *0* for the id of the desired task.
    """

    def list(self, request):
        data = OrderedDict({
            'practice task with task_id=three-steps-forward': reverse('practice_start_task',
                                                                      args=['three-steps-forward'], request=request),
            'recommend': reverse('practice_recommend', request=request)
        })
        return Response(data=data)


@allow_lazy_user
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def recommend(request):
    """
    Gets recommended task for the user
    """
    student = _get_or_create_student(request.user)
    with open_django_store() as store:
        try:
            task_id = select_task_fixed_then_random(store.state, student.student_id)
        except ValueError:
            task_id = None
    data = {
        'is_available': task_id is not None,
        'task_id': task_id
    }
    return Response(data=data)


@allow_lazy_user
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def start_task(request, task_id):
    """
    Starts practicing a selected task.
    """
    if request.method == 'GET':
        return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
    student = _get_or_create_student(request.user)
    task_session = _get_or_create_unfinished_task_session(student, task_id)
    data = {
        'task_session': reverse('task_session-detail', args=[task_session.pk], request=request)
    }
    return Response(data=data)


def _get_or_create_student(user):
    try:
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        with open_django_store(user=user) as store:
            action = actions.create_student()
            store.stage_action(action)
        student = Student.objects.get(user=user)
    return student


def _get_or_create_unfinished_task_session(student, task_id):
    try:
        task_session = TaskSession.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
        # TODO: check if the task session is not too old, in which case finish
        # it and start a new one
    except TaskSession.DoesNotExist:
        with open_django_store() as store:
            action = actions.start_task(student_id=student.student_id, task_id=task_id)
            store.stage_action(action)
        task_session = TaskSession.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
    return task_session
