# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0015_auto_20150418_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='tribe/static/tribe/photos/user_profiles', null=True),
            preserve_default=True,
        ),
    ]
