# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-18 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointer', '0002_auto_20170518_1521'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['-date']},
        ),
    ]
