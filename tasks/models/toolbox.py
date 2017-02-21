from django.db import models
from flocs import entities
from flocsweb.mixins import ExportMixin
from . import Block


class Toolbox(models.Model, ExportMixin):
    """ Model for a toolbox of Blockly blocks
    """
    named_tuple = entities.Toolbox

    toolbox_id = models.CharField(max_length=256, primary_key=True)
    blocks = models.ManyToManyField(Block)

    def __str__(self):
        return self.toolbox_id

    @staticmethod
    def import_entity(entity_tuple, *args, **kwargs):
        attributes = entity_tuple._asdict()
        del attributes['block_ids']
        toolbox = Toolbox(**attributes)
        toolbox.save()
        blocks = Block.objects.filter(pk__in=entity_tuple.block_ids)
        toolbox.blocks.add(*blocks)
        return toolbox
