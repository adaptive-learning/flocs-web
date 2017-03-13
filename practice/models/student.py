from django.db import models
from django.contrib.auth.models import User
from flocsweb.mixins import ImportExportMixin
from flocs import entities
from uuid import uuid4
from tasks.models import Instruction


class Student(models.Model, ImportExportMixin):
    """ Represents a learner (person practicing tasks)
    """
    entity_class = entities.Student

    student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User)
    seen_instructions = models.ManyToManyField(Instruction, through='SeenInstruction')


    @property
    def last_task_session_id(self):
        from .task_session import TaskSession
        try:
            return TaskSession.objects.filter(student=self).latest('creation_timestamp').task_session_id
        except TaskSession.DoesNotExist:
            return None

    def __str__(self):
        return '[{pk}] {username}'.format(pk=self.pk, username=self.user.username)

    @classmethod
    def import_entity(cls, entity, user=None, **kwargs):
        if user is None:
            user = cls.objects.get(student_id=entity.student_id).user
        return super().import_entity(entity, user=user, **kwargs)


class SeenInstruction(models.Model, ImportExportMixin):
    entity_class = entities.SeenInstruction

    seen_instruction_id = models.UUIDField(primary_key=True, default=uuid4)
    student = models.ForeignKey(Student)
    instruction = models.ForeignKey(Instruction)
