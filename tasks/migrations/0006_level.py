# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_toolbox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('credits', models.IntegerField()),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
