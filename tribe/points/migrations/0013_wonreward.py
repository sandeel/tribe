# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0009_auto_20150223_1937'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0012_reward'),
    ]

    operations = [
        migrations.CreateModel(
            name='WonReward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('reward', models.ForeignKey(related_name='wins', to='tribe.Tribe')),
                ('user', models.ForeignKey(related_name='rewards_won', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
