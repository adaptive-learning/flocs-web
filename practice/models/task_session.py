from datetime import datetime
from django.db import models
from flocsweb.mixins import ExportMixin
from flocs.entities import TaskSession
from tasks.models import Task
from uuid import uuid4
from .student import Student


class TaskSession(models.Model, ExportMixin):
    """
    A model for session of the task being practised by the student.
    """

    named_tuple = TaskSession

    task_session_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    student = models.ForeignKey(Student)

    task = models.ForeignKey(Task)

    creation_timestamp = models.DateTimeField(default=datetime.now, blank=True)

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
        return '[{pk}] {username} {task_id}'.format(pk=self.pk, username=self.student.user.username,
                                                    task_id=self.task.task_id)

    @staticmethod
    def import_entity(entity_tuple, *args, **kwargs):
        """
        Imports attribute values from named tuple and uses them as a input for constructor.
        Args:
            entity_tuple: named tuple with all the fields required by any of the class' constructor

        Returns: Instance of the class with the given data in attributes.

        """
        task_session = TaskSession(**entity_tuple._asdict())
        task_session.save()
        return task_session
