from django.db import models
from flocsweb.mixins import ImportExportMixin
from flocs.entities import TaskInstance
from .student import Student
from tasks.models import Task


class TaskInstance(models.Model, ImportExportMixin):
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

    def __str__(self):
        return '[{pk}] {username} {ref}'.format(pk=self.pk, username=self.student.user.username, ref=self.task.ref)
