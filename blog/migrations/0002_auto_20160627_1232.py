# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='createtime',
            field=models.DateTimeField(blank=True),
        ),
    ]