# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_block'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toolbox',
            fields=[
                ('toolbox_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('blocks', models.ManyToManyField(to='tasks.Block')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
