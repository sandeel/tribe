# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TribeUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('email', models.EmailField(max_length=255, verbose_name='email address', unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(to='auth.Group', verbose_name='groups', related_name='user_set', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'permissions': (('can_view', 'Can View'), ('can_modify', 'Can Modify')),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='tribeuser',
            name='leader_of',
            field=models.ForeignKey(related_name='leaders', null=True, to='tribe.Tribe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tribeuser',
            name='tribe',
            field=models.ForeignKey(null=True, to='tribe.Tribe'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tribeuser',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', verbose_name='user permissions', related_name='user_set', blank=True, related_query_name='user', help_text='Specific permissions for this user.'),
            preserve_default=True,
        ),
    ]
