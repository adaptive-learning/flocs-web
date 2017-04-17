# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0009_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksession',
            name='creation_timestamp',
        ),
    ]
