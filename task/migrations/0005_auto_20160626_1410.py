# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20160626_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='ren2',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ren2',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ren2',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]