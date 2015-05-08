# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tribe.models


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0010_auto_20150314_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeuser',
            name='image',
            field=models.ImageField(null=True, upload_to="", blank=True),
            preserve_default=True,
        ),
    ]
