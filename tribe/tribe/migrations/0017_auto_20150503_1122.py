# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0016_auto_20150418_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribe',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
