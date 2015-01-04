# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0006_auto_20150104_1445'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvitedEmail',
            new_name='InvitedUser',
        ),
    ]
