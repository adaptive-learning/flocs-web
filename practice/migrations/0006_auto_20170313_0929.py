# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0005_auto_20170313_0754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seeninstruction',
            old_name='instruction_id',
            new_name='instruction',
        ),
        migrations.RenameField(
            model_name='seeninstruction',
            old_name='student_id',
            new_name='student',
        ),
    ]
