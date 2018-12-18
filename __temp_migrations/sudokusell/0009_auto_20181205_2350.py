# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 12:50
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudokusell', '0008_auto_20181205_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='age',
            field=otree.db.models.StringField(choices=[(' 18-19', ' 18-19'), (' 20-21', ' 20-21'), (' 22-23', ' 22-23'), ('24-25', '24-25'), ('26 and older', '26 and older')], max_length=10000, null=True, verbose_name='א.\tמהו גילך '),
        ),
    ]