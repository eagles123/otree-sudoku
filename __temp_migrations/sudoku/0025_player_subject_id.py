# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-24 06:02
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0024_auto_20181211_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='subject_id',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]
