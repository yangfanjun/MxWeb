# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-04-16 19:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_int_user', models.IntegerField(default=0, verbose_name='用户ID')),
                ('id_int_course', models.IntegerField(default=0, verbose_name='课程ID')),
                ('rating', models.IntegerField(default=0, verbose_name='用户评分')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '用户评分',
                'verbose_name_plural': '用户评分',
            },
        ),
        migrations.CreateModel(
            name='WatchingTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_int_user', models.IntegerField(default=0, verbose_name='用户ID')),
                ('id_int_course', models.IntegerField(default=0, verbose_name='课程ID')),
                ('id_int_lesson', models.IntegerField(default=0, verbose_name='章节ID')),
                ('id_int_video', models.IntegerField(default=0, verbose_name='视频ID')),
                ('time', models.IntegerField(default=0, verbose_name='观看时长(秒)')),
                ('time_type', models.CharField(choices=[('1', '工作日上午'), ('2', '工作日下午'), ('3', '工作日晚间'), ('4', '工作日凌晨'), ('5', '周末上午'), ('6', '周末下午'), ('7', '周末晚间'), ('8', '周末凌晨'), ('9', '无')], default=1, max_length=20, verbose_name='时间类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='章节')),
            ],
            options={
                'verbose_name': '观看时长',
                'verbose_name_plural': '观看时长',
            },
        ),
    ]
