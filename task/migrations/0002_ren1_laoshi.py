# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(choices=[('c', 'yuwen'), ('a', 'shuxue'), ('b', 'wuli')], default='a', max_length=100),
        ),
    ]