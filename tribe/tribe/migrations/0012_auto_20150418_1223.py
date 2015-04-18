# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0011_tribeuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribeuser',
            name='image',
            field=models.ImageField(upload_to='photos/a', blank=True, null=True),
            preserve_default=True,
        ),
    ]
