# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_mei5'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mei6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('Time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Mei7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
