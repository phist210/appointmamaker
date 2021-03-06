# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-20 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointer', '0004_auto_20170518_1541'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['date', 'time']},
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
