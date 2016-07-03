# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 03:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0002_auto_20160702_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(default='', max_length=255)),
                ('sname', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='read.Series')),
            ],
        ),
    ]