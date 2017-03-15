# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.models


class Migration(migrations.Migration):

    dependencies = [
        ('flocsweb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='randomness',
            field=models.IntegerField(default=flocsweb.models.generate_random_integer),
        ),
    ]
