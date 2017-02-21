"""Fake models for tests
"""
from django.db import models
from flocs.tests.test_state import Entity
from flocsweb.mixins import ExportMixin

class DbEntity(models.Model, ExportMixin):
    named_tuple = Entity
    entity_id = models.CharField(max_length=256, primary_key=True)
    a = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return 'id={pk}'.format(pk=self.pk)

    @staticmethod
    def import_entity(entity_tuple):
        db_entity = DbEntity(**entity_tuple._asdict())
        db_entity.save()
        return db_entity
