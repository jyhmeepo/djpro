# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('webname', models.CharField(blank=True, default='', max_length=255)),
                ('weburl', models.CharField(blank=True, default='', max_length=255)),
                ('status', models.IntegerField(blank=True, default=1)),
                ('sort', models.IntegerField(blank=True, default=1)),
            ],
        ),
    ]
