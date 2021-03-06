# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 12:45
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudokusell', '0004_auto_20181205_2342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='experience',
        ),
        migrations.AddField(
            model_name='player',
            name='sudokoHobby',
            field=otree.db.models.StringField(choices=[('very much', 'very much'), ('to a great degree', 'to a great degree'), ('in some  ocassions', 'in some  ocassions'), ('rarely or not at all', 'rarely or not at all')], max_length=10000, null=True, verbose_name='Do you practice “word puzzles” and “number puzzles” as a hobby,'),
        ),
        migrations.AddField(
            model_name='player',
            name='wordNumberHobby',
            field=otree.db.models.StringField(choices=[('very much', 'very much'), ('to a great degree', 'to a great degree'), ('in some  ocassions', 'in some  ocassions'), ('rarely or not at all', 'rarely or not at all')], max_length=10000, null=True, verbose_name='Do you practice “word puzzles” and “number puzzles” as a hobby,'),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.StringField(choices=[('זכר', 'זכר'), ('נקבה', 'נקבה')], max_length=10000, null=True, verbose_name='ב.\tציין\\ח את מגדרך    גבר \\ אישה'),
        ),
    ]
