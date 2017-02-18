# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20161017_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category_id',
            field=models.CharField(max_length=256, default='uncategorized'),
        ),
    ]
