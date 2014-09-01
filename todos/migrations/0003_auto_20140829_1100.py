# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20140829_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='archived',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=None, to='todos.User'),
            preserve_default=False,
        ),
    ]
