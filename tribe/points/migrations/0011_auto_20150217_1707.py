# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0010_approval_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='date',
        ),
        migrations.AddField(
            model_name='approval',
            name='date_approved',
            field=models.DateField(auto_now=True, default=datetime.date(2015, 2, 17)),
            preserve_default=False,
        ),
    ]
