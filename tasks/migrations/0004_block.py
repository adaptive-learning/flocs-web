# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_category_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('block_id', models.CharField(primary_key=True, serialize=False, max_length=256)),
            ],
            bases=(models.Model, flocsweb.mixins.ExportMixin),
        ),
    ]
