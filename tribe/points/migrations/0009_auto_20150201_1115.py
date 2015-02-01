# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0008_approval'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approval',
            name='checkin',
        ),
        migrations.AddField(
            model_name='checkin',
            name='approval',
            field=models.OneToOneField(to='points.Approval', null=True),
            preserve_default=True,
        ),
    ]
