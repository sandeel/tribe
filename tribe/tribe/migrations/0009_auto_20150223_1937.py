# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0008_auto_20150112_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='name',
            field=models.CharField(default='User', max_length=40),
            preserve_default=True,
        ),
    ]
