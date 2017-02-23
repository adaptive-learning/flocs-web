# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('level', models.ForeignKey(to='tasks.Level')),
                ('toolbox', models.ForeignKey(to='tasks.Toolbox')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
    ]
