# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0007_auto_20150117_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='done',
            new_name='marked_done',
        ),
    ]
