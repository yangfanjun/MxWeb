# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2019-04-11 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20190405_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('1', 'Python'), ('2', 'Java'), ('3', 'C/C++'), ('4', 'Android'), ('5', '数据结构'), ('6', '人工智能')], default=1, max_length=20, verbose_name='课程类别'),
        ),
    ]