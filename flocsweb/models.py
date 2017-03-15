from random import randint
from django.db import models
from flocsweb.mixins import ImportExportMixin
from uuid import uuid4
from jsonfield import JSONField
from flocs import entities


def generate_random_integer(left=0, right=2**30):
    return randint(left, right)

class Action(models.Model, ImportExportMixin):
    """ Any action in our domain which we want to remember
    """
    entity_class = entities.Action

    action_id = models.UUIDField(primary_key=True, default=uuid4)
    type = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    randomness = models.IntegerField(default=generate_random_integer)
    version = models.CharField(max_length=100)
    data = JSONField()

    def __str__(self):
        return '[{pk}] {type}'.format(pk=self.pk, type=self.type)

    class Meta:
        ordering = ('time',)
