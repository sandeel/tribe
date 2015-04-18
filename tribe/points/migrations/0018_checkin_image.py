# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import points.models


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0017_auto_20150324_0533'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='image',
            field=models.ImageField(blank=True, upload_to=points.models.get_image_path, null=True),
            preserve_default=True,
        ),
    ]
