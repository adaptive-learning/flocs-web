from datetime import datetime
from uuid import uuid4
from django.db import models
from flocsweb.mixins import ImportExportMixin
from flocs import entities
from .student import Student


class Session(models.Model, ImportExportMixin):
    entity_class = entities.Session

    session_id = models.UUIDField(primary_key=True, default=uuid4)
    student = models.ForeignKey(Student, related_name='sessions')
    start = models.DateTimeField(default=datetime.now)
    end = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '[{pk}]'.format(pk=self.pk)
