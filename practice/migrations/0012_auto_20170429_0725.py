# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0011_programsnapshot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programsnapshot',
            old_name='task_session_id',
            new_name='task_session',
        ),
    ]
