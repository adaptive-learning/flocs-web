# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import flocsweb.mixins
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('action_id', models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('randomness', models.IntegerField()),
                ('version', models.CharField(max_length=100)),
                ('data', jsonfield.fields.JSONField()),
            ],
            options={
                'ordering': ('time',),
            },
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
