# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-27 12:23
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0025_player_subject_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='visit_websites',
            field=otree.db.models.StringField(default='0', max_length=10000, null=True),
        ),
    ]
