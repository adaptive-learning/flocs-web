from django.db import models
from django.contrib.auth.models import User
from flocsweb.mixins import ImportExportMixin
from flocs.entities import Student


class Student(models.Model, ImportExportMixin):
    """
    A model for a student (abstract person practicing tasks).
    """

    named_tuple = Student

    student_id = models.AutoField(primary_key=True)

    user = models.OneToOneField(User)

    def __str__(self):
        return '[{pk}] {username}'.format(pk=self.pk, username=self.user.username)

    def from_named_tuple(cls, tuple, user):
        try:
            return Student.objects.get(student_id=tuple.student_id)
        except Student.DoesNotExist:
            return Student(student_id=tuple.student_id, user=user)
