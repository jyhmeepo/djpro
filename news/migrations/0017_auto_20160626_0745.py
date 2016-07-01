# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_mei16'),
    ]

    operations = [
        migrations.AddField(
            model_name='mei16',
            name='time',
            field=models.TimeField(default='12:00:00'),
        ),
        migrations.AlterField(
            model_name='mei16',
            name='content',
            field=models.TextField(default='co'),
        ),
        migrations.AlterField(
            model_name='mei16',
            name='name',
            field=models.CharField(default='na', max_length=100),
        ),
    ]
