# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0020_task_date_available_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='available_to',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='available_rewards'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='assigned_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, related_name='tasks'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='friday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='monday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='saturday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='sunday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='thursday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='tuesday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='task',
            name='wednesday',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
