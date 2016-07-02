# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 05:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_art_createtime'),
    ]

    operations = [
        migrations.CreateModel(
            name='Que',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='QueT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tt', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='que',
            name='qt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.QueT'),
        ),
    ]
