# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0011_auto_20160627_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(choices=[('b', 'wuli'), ('c', 'yuwen'), ('a', 'shuxue')], max_length=100, default='a'),
        ),
    ]
