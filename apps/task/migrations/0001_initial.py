# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-04-15 20:43
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=30, verbose_name='任务标题')),
                ('task_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='任务详情')),
                ('task_price', models.FloatField(default=0.0, verbose_name='任务价格')),
                ('task_status', models.CharField(choices=[('0', '任务已取消'), ('1', '任务等待接受'), ('2', '任务已接受'), ('3', '已完成任务'), ('4', '任务超出截止日期'), ('5', '待审核任务')], max_length=10, verbose_name='任务状态')),
                ('task_type', models.BooleanField(default=False, verbose_name='接受任务或者发布任务')),
                ('task_deposit', models.IntegerField(verbose_name='任务押金金额')),
                ('task_deposit_status', models.IntegerField(verbose_name='任务押金状态')),
                ('task_updateTime', models.DateTimeField(auto_now=True, verbose_name='任务最近更新时间')),
                ('task_releaseTime', models.DateTimeField(auto_now_add=True, verbose_name='任务发布时间')),
                ('task_receiveTime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='任务领取时间')),
                ('task_deadline', models.DateTimeField(default=django.utils.timezone.now, verbose_name='任务截止时间')),
                ('task_extra', models.TextField(verbose_name='任务备注')),
                ('task_user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='任务用户')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
                'db_table': 'fb_task',
            },
        ),
        migrations.CreateModel(
            name='task_media',
            fields=[
                ('task_mediaId', models.AutoField(primary_key=True, serialize=False)),
                ('task_mediaurl', models.ImageField(blank=True, default='task_media/default.jpg', null=True, upload_to='task_media/', verbose_name='任务媒体资源')),
                ('task_index', models.IntegerField(verbose_name='任务媒体索引')),
                ('task_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_media', to='task.task', verbose_name='所属任务id')),
            ],
            options={
                'verbose_name': '任务媒体',
                'verbose_name_plural': '任务媒体',
                'db_table': 'fb_task_media',
            },
        ),
    ]
