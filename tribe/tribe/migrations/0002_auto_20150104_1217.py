# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tribe',
            options={},
        ),
        migrations.AddField(
            model_name='tribeuser',
            name='name',
            field=models.CharField(max_length=40, default='Daniel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tribeuser',
            name='tribe',
            field=models.ForeignKey(to='tribe.Tribe', null=True, related_name='members'),
            preserve_default=True,
        ),
    ]
