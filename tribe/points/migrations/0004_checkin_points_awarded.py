# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0003_checkin_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin',
            name='points_awarded',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
