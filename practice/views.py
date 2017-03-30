from collections import OrderedDict
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view, permission_classes
from lazysignup.decorators import allow_lazy_user
from flocs import actions, recommendation
from flocsweb.store import open_django_store
from tasks.models import Task
from .serializers import StudentSerializer, TaskSessionSerializer
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


class PracticeViewSet(viewsets.GenericViewSet):
    """
    This page does not do anything. You can perform any of the following actions.

    - get a task id of based on system's recommendation
    - practice a specific task of your choice

    In case of practicing a specific task, substitute *0* for the id of the desired task.
    """

    def list(self, request):
        data = OrderedDict([
            ('get_or_create_student',
                reverse('practice_get_or_create_student', request=request)),
            ('start_task (example)',
                reverse('practice_start_task', args=['three-steps-forward'], request=request)),
            ('see_instruction',
                reverse('practice_see_instruction', request=request)),
            ('recommend',
                reverse('practice_recommend', request=request)),
        ])
        return Response(data=data)


@allow_lazy_user
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def recommend(request):
    """
    Gets recommended task for the user
    """
    student = _get_or_create_student(request)
    with open_django_store() as store:
        try:
            task_id = recommendation.fixed_then_random(store.state, student.student_id)
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
def get_or_create_student(request):
    """
    Return a student object for current user
    """
    if request.method == 'GET':
        return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
    student = _get_or_create_student(request)
    student_url = reverse('student-detail', args=[student.pk], request=request)
    data = {
        'student_url': student_url,
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
    student = _get_or_create_student(request)
    task_session = _get_or_create_unfinished_task_session(student, task_id)
    data = {
        'task_session': reverse('task_session-detail', args=[task_session.pk], request=request)
    }
    return Response(data=data)


@allow_lazy_user
@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated])
def see_instruction(request):
    """
    Student was presented an instruction
    """
    if request.method == 'GET':
        return Response("Use POST method.", status=status.HTTP_204_NO_CONTENT)
    with open_django_store() as store:
        action = actions.create(
            type='see-instruction',
            data={
                'student-id': request.data['student_id'],
                'instruction-id': request.data['instruction_id']})
        store.stage_action(action)
    return Response(status=status.HTTP_204_NO_CONTENT)


def _get_or_create_student(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        with open_django_store(request=request) as store:
            action = actions.create(type='create-student', data={})
            store.stage_action(action)
        student = Student.objects.get(user=request.user)
    return student


def _get_or_create_unfinished_task_session(student, task_id):
    try:
        task_session = TaskSession.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
        # TODO: check if the task session is not too old, in which case finish
        # it and start a new one
    except TaskSession.DoesNotExist:
        with open_django_store() as store:
            action = actions.create(
                type='start-task',
                data={'student-id': student.student_id, 'task-id': task_id})
            store.stage_action(action)
        task_session = TaskSession.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
    return task_session
