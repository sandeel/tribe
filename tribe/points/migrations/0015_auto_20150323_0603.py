# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0014_auto_20150311_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='AchievedReward',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('reward', models.ForeignKey(to='points.Reward', related_name='wins')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='rewards_won')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='wonreward',
            name='reward',
        ),
        migrations.RemoveField(
            model_name='wonreward',
            name='user',
        ),
        migrations.DeleteModel(
            name='WonReward',
        ),
    ]
