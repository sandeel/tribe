# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0007_auto_20150104_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inviteduser',
            name='tribe',
            field=models.ForeignKey(related_name='invited_users', to='tribe.Tribe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tribe',
            name='name',
            field=models.CharField(max_length=255, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tribeuser',
            name='tribe',
            field=models.ForeignKey(null=True, to='tribe.Tribe', on_delete=django.db.models.deletion.SET_NULL, related_name='members'),
            preserve_default=True,
        ),
    ]
