# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0006_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tasktemplate',
            name='assigned_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='tasks'),
            preserve_default=True,
        ),
    ]
