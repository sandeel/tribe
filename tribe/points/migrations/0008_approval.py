# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0007_auto_20150129_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('approver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='approvals')),
                ('checkin', models.OneToOneField(related_name='approval', to='points.CheckIn')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
