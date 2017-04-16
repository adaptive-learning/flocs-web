# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_instruction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(to='tasks.Category', null=True, default=None, related_name='tasks'),
        ),
    ]
