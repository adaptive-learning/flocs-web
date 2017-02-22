from datetime import datetime
from django.db import models
from flocsweb.mixins import ImportExportMixin
from flocs import entities
from tasks.models import Task
from uuid import uuid4
from .student import Student


class TaskSession(models.Model, ImportExportMixin):
    """ A model for session of the task being practised by the student
    """
    entity_class = entities.TaskSession

    task_session_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    student = models.ForeignKey(Student)
    task = models.ForeignKey(Task)
    creation_timestamp = models.DateTimeField(default=datetime.now, blank=True)
    solved = models.BooleanField(default=False)
    given_up = models.BooleanField(default=False)

    @property
    def is_active(self):
        return not self.solved and not self.given_up

    def __str__(self):
        return '[{pk}] {username} {task_id}'.format(pk=self.pk, username=self.student.user.username,
                                                    task_id=self.task.task_id)
