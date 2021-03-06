# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-22 10:04
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0007_player_game_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='game_attempt',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='game_correct',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]
