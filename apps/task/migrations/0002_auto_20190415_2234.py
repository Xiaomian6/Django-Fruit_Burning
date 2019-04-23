# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190415_2043'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='task_user',
        ),
        migrations.AddField(
            model_name='task',
            name='task_role',
            field=models.ManyToManyField(blank=True, to='user.role', verbose_name='任务角色'),
        ),
    ]
