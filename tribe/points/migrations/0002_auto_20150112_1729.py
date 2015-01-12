# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tribe', '0008_auto_20150112_1729'),
        ('points', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTemplate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='points.Category')),
                ('tribe', models.ForeignKey(related_name='task_templates', to='tribe.Tribe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=500, default='Description goes here.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='tribe',
            field=models.ForeignKey(to='tribe.Tribe', default=1, related_name='categories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
