# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-06 10:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudokusell', '0016_auto_20181206_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='is_terminated',
        ),
    ]