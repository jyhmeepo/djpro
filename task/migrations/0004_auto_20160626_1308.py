# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20160626_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='ren2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(choices=[('c', 'yuwen'), ('a', 'shuxue'), ('b', 'wuli')], default='a', max_length=100),
        ),
    ]
