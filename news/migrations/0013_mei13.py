# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20160626_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mei13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FilePathField()),
            ],
        ),
    ]
