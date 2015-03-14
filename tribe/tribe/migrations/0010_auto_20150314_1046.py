# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0009_auto_20150223_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='name',
            field=models.CharField(max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tribeuser',
            name='tribe',
            field=models.ForeignKey(default=1, related_name='members', to='tribe.Tribe'),
            preserve_default=False,
        ),
    ]
