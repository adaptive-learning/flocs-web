# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
        migrations.CreateModel(
            name='TaskInstance',
            fields=[
                ('task_instance_id', models.UUIDField(serialize=False, editable=False, default=uuid.uuid4, primary_key=True)),
                ('solved', models.BooleanField(default=False)),
                ('given_up', models.BooleanField(default=False)),
                ('student', models.ForeignKey(to='practice.Student')),
                ('task', models.ForeignKey(to='tasks.Task')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
