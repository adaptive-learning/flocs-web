from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin


class Block(models.Model, ImportExportMixin):
    """ Model for a Blockly block
    """
    entity_class = entities.Block

    block_id = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.block_id
