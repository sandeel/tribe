# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0003_invitedemails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvitedEmails',
            new_name='InvitedEmail',
        ),
    ]
