# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-25 01:51
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0011_auto_20181125_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='game_attemptted',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
