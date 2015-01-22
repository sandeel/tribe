# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0008_auto_20150112_1729'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('points', '0008_auto_20150117_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktemplate',
            name='assigned_users',
        ),
        migrations.RemoveField(
            model_name='tasktemplate',
            name='category',
        ),
        migrations.RemoveField(
            model_name='tasktemplate',
            name='tribe',
        ),
        migrations.RemoveField(
            model_name='task',
            name='marked_done',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_template',
        ),
        migrations.DeleteModel(
            name='TaskTemplate',
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='task_templates'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ForeignKey(default=0, to='points.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.CharField(max_length=200, default='Description goes here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=200, default='Task'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='points_reward',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='recurring_strategy',
            field=models.CharField(max_length=200, default='Always'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='tribe',
            field=models.ForeignKey(to='tribe.Tribe', related_name='task_templates', default=0),
            preserve_default=False,
        ),
    ]
