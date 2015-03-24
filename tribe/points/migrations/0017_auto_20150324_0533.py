# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0016_auto_20150324_0531'),
    ]

    operations = [
        migrations.CreateModel(
            name='RewardCashIn',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('achievedReward', models.ForeignKey(to='points.AchievedReward', related_name='cashins')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='cashedinreward',
            name='achievedReward',
        ),
        migrations.DeleteModel(
            name='CashedInReward',
        ),
    ]
