# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0015_auto_20150323_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='CashedInReward',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('achievedReward', models.ForeignKey(to='points.AchievedReward', related_name='cashins')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='achievedreward',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='achieved_rewards'),
            preserve_default=True,
        ),
    ]
