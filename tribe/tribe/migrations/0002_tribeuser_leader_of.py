# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tribeuser',
            name='leader_of',
            field=models.ForeignKey(null=True, to='tribe.Tribe', related_name='leaders'),
            preserve_default=True,
        ),
    ]
