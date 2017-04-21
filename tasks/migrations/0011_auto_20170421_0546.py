# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20170416_0544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='block',
            name='order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
