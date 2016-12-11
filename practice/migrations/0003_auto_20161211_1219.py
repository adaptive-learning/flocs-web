# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0002_taskinstance_creation_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskinstance',
            old_name='task_instance_id',
            new_name='task_session_id',
        ),
    ]
