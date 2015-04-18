# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0013_auto_20150418_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='tribe/static/tribe/photos/user_profiles'),
            preserve_default=True,
        ),
    ]
