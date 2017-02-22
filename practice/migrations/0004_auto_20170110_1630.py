# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins
import uuid
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20161017_1742'),
        ('practice', '0003_auto_20161211_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskSession',
            fields=[
                ('task_session_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('creation_timestamp', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('solved', models.BooleanField(default=False)),
                ('given_up', models.BooleanField(default=False)),
                ('student', models.ForeignKey(to='practice.Student')),
                ('task', models.ForeignKey(to='tasks.Task')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
        migrations.RemoveField(
            model_name='taskinstance',
            name='student',
        ),
        migrations.RemoveField(
            model_name='taskinstance',
            name='task',
        ),
        migrations.DeleteModel(
            name='TaskInstance',
        ),
    ]
