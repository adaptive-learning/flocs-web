from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin


class Task(models.Model, ImportExportMixin):
    """ Model for a task (exercise)
    """
    named_tuple = entities.Task

    task_id = models.AutoField(primary_key=True)

    ref = models.TextField()

    def __str__(self):
        return '[{pk}] {ref}'.format(pk=self.pk, ref=self.ref)
