# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0005_auto_20150128_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='task',
            name='wednesday',
        ),
    ]
