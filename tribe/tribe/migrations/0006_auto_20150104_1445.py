# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0005_remove_invitedemail_tribe'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitedemail',
            name='tribe',
            field=models.ForeignKey(default=1, to='tribe.Tribe', related_name='invited_emails'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invitedemail',
            name='email',
            field=models.EmailField(max_length=75, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tribe',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
