# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_mei16_fa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mei16',
            name='time',
            field=models.TimeField(blank=True, default='12:00:00'),
        ),
    ]