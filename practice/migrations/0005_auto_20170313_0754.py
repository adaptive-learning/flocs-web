# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import flocsweb.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_instruction'),
        ('practice', '0004_auto_20170110_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeenInstruction',
            fields=[
                ('seen_instruction_id', models.UUIDField(serialize=False, primary_key=True, default=uuid.uuid4)),
                ('instruction_id', models.ForeignKey(to='tasks.Instruction')),
                ('student_id', models.ForeignKey(to='practice.Student')),
            ],
            bases=(models.Model, flocsweb.mixins.ImportExportMixin),
        ),
        migrations.AddField(
            model_name='student',
            name='seen_instructions',
            field=models.ManyToManyField(through='practice.SeenInstruction', to='tasks.Instruction'),
        ),
    ]
