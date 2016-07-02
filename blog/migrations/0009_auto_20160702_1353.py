# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_inv_project2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=255)),
                ('old', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Xm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xname', models.CharField(default='', max_length=255)),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='inv',
            name='project2',
            field=models.CharField(choices=[('xm1', 'shiyou'), ('xm2', 'dianxin')], default='', max_length=255),
        ),
    ]