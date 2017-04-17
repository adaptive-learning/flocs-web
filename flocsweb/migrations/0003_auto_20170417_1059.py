# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flocsweb', '0002_auto_20170313_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
