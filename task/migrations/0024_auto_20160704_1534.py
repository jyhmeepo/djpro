# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0023_auto_20160703_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(max_length=100, default='a', choices=[('a', 'shuxue'), ('b', 'wuli'), ('c', 'yuwen')]),
        ),
    ]
