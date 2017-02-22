from django.db import models
from django.contrib.auth.models import User
from flocsweb.mixins import ImportExportMixin
from flocs import entities
from uuid import uuid4


class Student(models.Model, ImportExportMixin):
    """ Represents a learner (person practicing tasks)
    """
    entity_class = entities.Student

    student_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User)

    @property
    def last_task_session(self):
        from .task_session import TaskSession
        try:
            return TaskSession.objects.filter(student=self).latest('creation_timestamp').task_session_id
        except TaskSession.DoesNotExist:
            return None

    def __str__(self):
        return '[{pk}] {username}'.format(pk=self.pk, username=self.user.username)

    @staticmethod
    def import_entity(entity, user=None, **kwargs):
        if user is None:
            user = Student.objects.get(student_id=entity.student_id).user
        student = Student(**entity._asdict(), user=user)
        student.save()
        return student
