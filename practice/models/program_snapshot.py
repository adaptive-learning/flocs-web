from datetime import datetime
from uuid import uuid4
from django.db import models
from flocsweb.mixins import ImportExportMixin
from flocs import entities
from .task_session import TaskSession


class ProgramSnapshot(models.Model, ImportExportMixin):
    entity_class = entities.ProgramSnapshot

    program_snapshot_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    task_session = models.ForeignKey(TaskSession, related_name='snapshots')
    order = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)
    program = models.TextField()
    execution = models.BooleanField(default=False)
    correct = models.NullBooleanField(default=None)

    @property
    def program_shortened(self):
        if len(self.program) > 60:
            return self.program[:60] + '...'
        return self.program

    def __str__(self):
        return '[{pk}] {program}'.format(pk=self.pk, program=self.program_shortened)
