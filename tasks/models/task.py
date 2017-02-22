from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin
from jsonfield import JSONField


class Task(models.Model, ImportExportMixin):
    """ Model for a task (problem) to be solved by students
    """
    entity_class = entities.Task

    task_id = models.CharField(max_length=256, primary_key=True)
    category_id = models.CharField(max_length=256, default='uncategorized')
        # TODO: replace by a category once we introduce Category model
    setting = JSONField()
    solution = JSONField()

    def __str__(self):
        return self.task_id
