# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0004_auto_20150104_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitedemail',
            name='tribe',
        ),
    ]
