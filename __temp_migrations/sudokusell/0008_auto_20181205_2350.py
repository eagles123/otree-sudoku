# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-05 12:50
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('sudokusell', '0007_auto_20181205_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='wordNumberHobby',
            field=otree.db.models.StringField(choices=[('הרבה פעמים', 'הרבה פעמים'), ('לעתים קרובות', 'לעתים קרובות'), ('מדי פעם', 'מדי פעם'), ('באופן נדיר', 'באופן נדיר'), ('אף פעם לא', 'אף פעם לא')], max_length=10000, null=True, verbose_name='ד.\tהאם בעבר פתרת משחקי אותיות או מספרים כתחביב? '),
        ),
    ]
