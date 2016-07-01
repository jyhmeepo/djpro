# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_auto_20160626_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ren1',
            name='laoshi',
            field=models.CharField(default='a', max_length=100, choices=[('c', 'yuwen'), ('a', 'shuxue'), ('b', 'wuli')]),
        ),
    ]
