from django.db import models
from flocs import entities
from flocsweb.mixins import ExportMixin
from jsonfield import JSONField


class Task(models.Model, ExportMixin):
    """
    Model for a task (exercise)
    """
    named_tuple = entities.Task

    task_id = models.CharField(max_length=256, primary_key=True)
    category_id = models.CharField(max_length=256, default='uncategorized')
        # TODO: replace by a category once we introduce Category model
    setting = JSONField()
    solution = JSONField()

    def __str__(self):
        return self.task_id

    @staticmethod
    def from_named_tuple(entity_tuple, *args, **kwargs):
        """
        Imports attribute values from named tuple and uses them as a input for constructor.
        Args:
            entity_tuple: named tuple with all the fields required by any of the class' constructor

        Returns: Instance of the class with the given data in attributes.

        """
        return Task(**entity_tuple._asdict())
