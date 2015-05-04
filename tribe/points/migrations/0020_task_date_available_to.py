# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0019_auto_20150418_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_available_to',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
