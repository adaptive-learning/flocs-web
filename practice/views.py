from collections import OrderedDict
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view, permission_classes
from lazysignup.decorators import allow_lazy_user
from .serializers import StudentSerializer, TaskInstanceSerializer
from .models import Student, TaskInstance
from .permissions import IsAdminOrOwnerPostAnyone
from flocs import actions
from flocs.recommendation import recommend_task
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


class TaskInstancesViewSet(viewsets.ModelViewSet):
    """
    This view presents task instances.

    Regular users can only access their own instances. Staff members can see all the instances.
    """

    serializer_class = TaskInstanceSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrOwnerPostAnyone]

    def get_queryset(self):
        """
        Filter out instances that current user has not access to.
        """
        user = self.request.user
        if user and user.is_staff:
            return TaskInstance.objects.all()
        return TaskInstance.objects.filter(student__user=user)

    @detail_route(methods=['POST'])
    def solve_task(self, request, pk=None):
        if not self.get_object().is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="This task instance is already closed.")
        with open_django_store() as store:
            action = actions.solve_task(pk)
            store.stage_action(action)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @detail_route(methods=['POST'])
    def give_up_task(self, request, pk=None):
        if not self.get_object().is_active:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="This task instance already closed.")
        with open_django_store() as store:
            action = actions.give_up_task(pk)
            store.stage_action(action)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PracticeViewSet(viewsets.GenericViewSet):
    """
    This page does not do anything. You can perform any of the following actions.

    - start practicing task base on system's recommendation
    - practice a specific task of your choice

    In case of practicing a specific task, substitute *0* for the id of the desired task.
    """

    def list(self, request):
        data = OrderedDict({
            'start practicing': reverse('practice_start', request=request),
            'practice task with task_id=three-steps-forward': reverse('practice_start_task',
                                                                      args=['three-steps-forward'], request=request)
        })
        return Response(data=data)


@allow_lazy_user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def start(request):
    """
    Starts practicing a task selected by system's recommender system.
    """
    student = _get_or_create_student(request.user)
    task = recommend_task(
        student.to_named_tuple(),
        list(map(lambda x: x.to_named_tuple(), Task.objects.all())),
        []
    )
    task_id = task.task_id
    task_instance = _get_or_create_task_instance(student, task_id)
    data = {
        'task_instance': reverse('task_instance-detail', args=[task_instance.pk], request=request)
    }
    return Response(data=data)


@allow_lazy_user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def start_task(request, task_id):
    """
    Starts practicing a selected task.
    """
    student = _get_or_create_student(request.user)
    task_instance = _get_or_create_task_instance(student.student_id, task_id)
    data = {
        'task_instance': reverse('task_instance-detail', args=[task_instance.pk], request=request)
    }
    return Response(data=data)


def _get_or_create_student(user):
    try:
        student = Student.objects.get(user=user)
    except Student.DoesNotExist:
        with open_django_store({'user': user}) as store:
            action = actions.create_student()
            store.stage_action(action)
        student = Student.objects.get(user=user)
    return student


def _get_or_create_task_instance(student, task_id):
    try:
        task_instance = TaskInstance.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
    except TaskInstance.DoesNotExist:
        with open_django_store() as store:
            action = actions.start_task(student_id=student.student_id, task_id=task_id)
            store.stage_action(action)
        task_instance = TaskInstance.objects.get(student=student, task__task_id=task_id, solved=False, given_up=False)
    return task_instance
