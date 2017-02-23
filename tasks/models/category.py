from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin
from . import Level, Toolbox


class Category(models.Model, ImportExportMixin):
    """ Group of a few tasks of similar difficulty and topic and with same toolbox
    """
    entity_class = entities.Category

    category_id = models.CharField(max_length=256, primary_key=True)
    level = models.ForeignKey(Level)
    toolbox = models.ForeignKey(Toolbox)

    def __str__(self):
        return self.category_id
