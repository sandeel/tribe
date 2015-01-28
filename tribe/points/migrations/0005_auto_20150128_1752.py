# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0004_checkin_points_awarded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
