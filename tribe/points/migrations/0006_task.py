# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0005_tasktemplate_assigned_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('task_template', models.ForeignKey(to='points.TaskTemplate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
