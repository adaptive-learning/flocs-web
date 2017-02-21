from django.db import models
from flocs import entities
from flocsweb.mixins import ExportMixin


class Block(models.Model, ExportMixin):
    """ Model for a Blockly block
    """
    named_tuple = entities.Block

    block_id = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.block_id

    @staticmethod
    def import_entity(entity_tuple, *args, **kwargs):
        block = Block(**entity_tuple._asdict())
        block.save()
        return block
