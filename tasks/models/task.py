from django.db import models
from flocs import entities
from flocsweb.mixins import ExportMixin


class Task(models.Model, ExportMixin):
    """
    Model for a task (exercise)
    """
    named_tuple = entities.Task

    task_id = models.AutoField(primary_key=True)

    ref = models.TextField()

    def __str__(self):
        return '[{pk}] {ref}'.format(pk=self.pk, ref=self.ref)

    @staticmethod
    def from_named_tuple(entity_tuple, *args, **kwargs):
        """
        Imports attribute values from named tuple and uses them as a input for constructor.
        Args:
            entity_tuple: named tuple with all the fields required by any of the class' constructor

        Returns: Instance of the class with the given data in attributes.

        """
        return Task(**entity_tuple._asdict())
