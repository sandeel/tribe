# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0002_auto_20150104_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=75)),
                ('tribe', models.ForeignKey(to='tribe.Tribe', related_name='invited_emails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
