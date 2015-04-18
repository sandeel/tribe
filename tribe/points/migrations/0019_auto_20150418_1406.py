# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0018_checkin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='image',
            field=models.ImageField(blank=True, upload_to='tribe/static/tribe/photos/checkins', null=True),
            preserve_default=True,
        ),
    ]
