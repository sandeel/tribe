# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_auto_20150112_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktemplate',
            name='description',
            field=models.CharField(max_length=200, default='Description of the task goes here.'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
