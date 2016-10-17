# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import flocsweb.mixins
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('setting', jsonfield.fields.JSONField()),
                ('solution', jsonfield.fields.JSONField()),
            ],
            bases=(models.Model, flocsweb.mixins.ExportMixin),
        ),
    ]
