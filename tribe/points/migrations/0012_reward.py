# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0009_auto_20150223_1937'),
        ('points', '0011_auto_20150217_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('tribe', models.ForeignKey(to='tribe.Tribe', related_name='rewards')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
