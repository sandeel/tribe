# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0014_auto_20150418_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/tribe/photos/user_profiles', null=True),
            preserve_default=True,
        ),
    ]
