# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0016_auto_20160702_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(choices=[('a', 'shuxue'), ('b', 'wuli'), ('c', 'yuwen')], default='a', max_length=100),
        ),
    ]
