# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-04-16 19:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchingtime',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='watchingtime',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Video', verbose_name='视频'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='课程'),
        ),
        migrations.AddField(
            model_name='userrating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
