from django.db import models
from flocs import entities
from flocsweb.mixins import ImportExportMixin


class Instruction(models.Model, ImportExportMixin):
    entity_class = entities.Instruction

    instruction_id = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.instruction_id
