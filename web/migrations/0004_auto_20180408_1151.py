# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-08 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20180408_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='assets_price',
            new_name='buying_price',
        ),
    ]
