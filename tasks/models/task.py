from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin
from jsonfield import JSONField
from . import Category


class Task(models.Model, ImportExportMixin):
    """ Model for a task (problem) to be solved by students
    """
    entity_class = entities.Task

    task_id = models.CharField(max_length=256, primary_key=True)
    category = models.ForeignKey(Category, null=True, default=None)
    setting = JSONField()
    solution = JSONField()

    def __str__(self):
        return self.task_id
