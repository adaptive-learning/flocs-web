from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin


class Level(models.Model, ImportExportMixin):
    """ Global difficulty level of a task, or global skill level of a student
    """
    entity_class = entities.Level

    level_id = models.SmallIntegerField(primary_key=True)
    credits = models.IntegerField()

    def __str__(self):
        return 'L' + str(self.level_id)
