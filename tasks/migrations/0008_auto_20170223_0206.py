# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category_id',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, to='tasks.Category', default=None),
        ),
    ]
