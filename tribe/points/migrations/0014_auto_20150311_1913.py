# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0013_wonreward'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='available_to',
            field=models.ManyToManyField(related_name='available_rewards', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='reward',
            name='points_required',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
