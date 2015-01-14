# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_auto_20150112_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktemplate',
            name='points_reward',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasktemplate',
            name='recurring_strategy',
            field=models.CharField(default='every week', max_length=200),
            preserve_default=False,
        ),
    ]
