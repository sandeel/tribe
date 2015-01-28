# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkin',
            name='time',
        ),
        migrations.AlterField(
            model_name='task',
            name='date_available',
            field=models.DateField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='time_available_from',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='time_available_to',
            field=models.TimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
