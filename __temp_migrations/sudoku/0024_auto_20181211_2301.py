# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-11 12:01
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0023_player_visit_websites'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_demo',
            field=otree.db.models.StringField(default='0', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='second_demo',
            field=otree.db.models.StringField(default='0', max_length=10000, null=True),
        ),
    ]