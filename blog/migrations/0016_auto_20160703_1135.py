# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160703_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv',
            name='project2',
            field=models.CharField(choices=[('xm2', 'dianxin'), ('xm1', 'shiyou')], default='', max_length=255),
        ),
    ]