from django.db import models
from django.contrib.auth.models import User
from flocsweb.mixins import ExportMixin
from flocs.entities import Student as Student_tuple
from uuid import uuid4


class Student(models.Model, ExportMixin):
    """
    A model for a student (abstract person practicing tasks).
    """

    named_tuple = Student_tuple

    student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    user = models.OneToOneField(User)

    @property
    def last_task_session(self):
        from .task_instance import TaskInstance
        try:
            return TaskInstance.objects.filter(student=self).latest('creation_timestamp')
        except TaskInstance.DoesNotExist:
            return None

    def __str__(self):
        return '[{pk}] {username}'.format(pk=self.pk, username=self.user.username)

    @staticmethod
    def from_named_tuple(entity_tuple, user, **kwargs):
        try:
            return Student.objects.get(student_id=entity_tuple.student_id)
        except Student.DoesNotExist:
            return Student(student_id=entity_tuple.student_id, user=user)
