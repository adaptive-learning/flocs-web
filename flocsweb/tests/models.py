"""Fake models for tests
"""
from django.db import models
from flocs.tests.test_state import TestEntityMapping
from flocsweb.mixins import ExportMixin

class Entity(models.Model, ExportMixin):
    named_tuple = TestEntityMapping.entity_class
    entity_id = models.CharField(max_length=256, primary_key=True)
    a = models.IntegerField()
    b = models.IntegerField()

    @staticmethod
    def from_named_tuple(entity_tuple):
        return Entity(**entity_tuple._asdict())
