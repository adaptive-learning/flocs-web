# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import flocsweb.mixins
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0008_auto_20170415_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('start', models.DateTimeField(default=datetime.datetime.now)),
                ('end', models.DateTimeField(default=datetime.datetime.now)),
                ('student', models.ForeignKey(to='practice.Student', related_name='sessions')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
