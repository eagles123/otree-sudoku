# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-25 02:36
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0013_auto_20181125_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='price',
            field=otree.db.models.FloatField(null=True),
        ),
    ]
