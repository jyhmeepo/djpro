# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_mei'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mei2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('content2', models.TextField()),
            ],
        ),
    ]