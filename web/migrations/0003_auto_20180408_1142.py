# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-08 03:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180408_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='assets_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
