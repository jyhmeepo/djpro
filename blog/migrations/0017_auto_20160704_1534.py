# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20160703_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inv',
            name='project2',
            field=models.CharField(max_length=255, default='', choices=[('xm1', 'shiyou'), ('xm2', 'dianxin')]),
        ),
    ]
