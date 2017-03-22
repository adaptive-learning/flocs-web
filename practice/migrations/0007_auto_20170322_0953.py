# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0006_auto_20170313_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tasksession',
            name='student',
            field=models.ForeignKey(to='practice.Student', related_name='task_sessions'),
        ),
    ]
