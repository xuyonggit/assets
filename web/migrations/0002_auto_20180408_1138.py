# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-08 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='assets_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='asset',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
