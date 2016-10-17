from django.db import models
from django.contrib.auth.models import User
from flocsweb.mixins import ExportMixin
from flocs.entities import Student
from uuid import uuid4


class Student(models.Model, ExportMixin):
    """
    A model for a student (abstract person practicing tasks).
    """

    named_tuple = Student

    student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    user = models.OneToOneField(User)

    def __str__(self):
        return '[{pk}] {username}'.format(pk=self.pk, username=self.user.username)

    @staticmethod
    def from_named_tuple(entity_tuple, user, **kwargs):
        try:
            return Student.objects.get(student_id=entity_tuple.student_id)
        except Student.DoesNotExist:
            return Student(student_id=entity_tuple.student_id, user=user)
