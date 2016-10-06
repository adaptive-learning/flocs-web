from django.db import models
from flocsweb.mixins import ExportMixin
from flocs.entities import TaskInstance
from .student import Student
from tasks.models import Task


class TaskInstance(models.Model, ExportMixin):
    """
    A model for instance of the task being practised by the student.
    """

    named_tuple = TaskInstance

    task_instance_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(Student)

    task = models.ForeignKey(Task)

    solved = models.BooleanField(
        default=False
    )

    given_up = models.BooleanField(
        default=False
    )

    @property
    def is_active(self):
        return not self.solved and not self.given_up

    def __str__(self):
        return '[{pk}] {username} {ref}'.format(pk=self.pk, username=self.student.user.username, ref=self.task.ref)

    @staticmethod
    def from_named_tuple(entity_tuple, *args, **kwargs):
        """
        Imports attribute values from named tuple and uses them as a input for constructor.
        Args:
            entity_tuple: named tuple with all the fields required by any of the class' constructor

        Returns: Instance of the class with the given data in attributes.

        """
        student = Student.objects.get(pk=entity_tuple.student_id)
        task = Task.objects.get(pk=entity_tuple.task_id)
        return TaskInstance(**entity_tuple._asdict())
