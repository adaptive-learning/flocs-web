# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0007_auto_20170322_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasksession',
            name='end',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tasksession',
            name='start',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
