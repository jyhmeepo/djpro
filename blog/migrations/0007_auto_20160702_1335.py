# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160702_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv',
            name='iname',
            field=models.CharField(default='', max_length=255, verbose_name='inv name'),
        ),
    ]