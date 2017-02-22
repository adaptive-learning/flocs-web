from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin
from . import Block


class Toolbox(models.Model, ImportExportMixin):
    """ Model for a toolbox of Blockly blocks
    """
    entity_class = entities.Toolbox

    toolbox_id = models.CharField(max_length=256, primary_key=True)
    blocks = models.ManyToManyField(Block)

    def __str__(self):
        return self.toolbox_id
