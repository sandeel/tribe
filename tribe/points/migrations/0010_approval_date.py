# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0009_auto_20150201_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='approval',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 17, 16, 55, 22, 323260, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
