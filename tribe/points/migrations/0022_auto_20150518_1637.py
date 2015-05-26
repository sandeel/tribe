# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0021_auto_20150505_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='approval',
            field=models.OneToOneField(null=True, to='points.Approval', blank=True),
            preserve_default=True,
        ),
    ]
