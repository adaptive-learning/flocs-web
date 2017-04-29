# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_remove_tasksession_creation_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramSnapshot',
            fields=[
                ('program_snapshot_id', models.UUIDField(serialize=False, editable=False, primary_key=True, default=uuid.uuid4)),
                ('order', models.IntegerField()),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('program', models.TextField()),
                ('execution', models.BooleanField(default=False)),
                ('correct', models.NullBooleanField(default=None)),
                ('task_session_id', models.ForeignKey(related_name='snapshots', to='practice.TaskSession')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
