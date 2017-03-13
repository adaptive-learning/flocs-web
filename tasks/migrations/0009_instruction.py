# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20170223_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('instruction_id', models.CharField(primary_key=True, serialize=False, max_length=256)),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
