# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-24 11:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_auto_20190415_2234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_role',
            new_name='role',
        ),
    ]