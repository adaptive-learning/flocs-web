"""Fake models for tests
"""
from django.db import models
from flocs.tests.test_state import Entity
from flocsweb.mixins import ImportExportMixin

class DbEntity(models.Model, ImportExportMixin):
    entity_class = Entity
    entity_id = models.CharField(max_length=256, primary_key=True)
    a = models.IntegerField()
    b = models.IntegerField()

    def __str__(self):
        return 'id={pk}'.format(pk=self.pk)
