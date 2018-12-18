import csv

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kevin Feng'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sudokusell'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    seat_number = models.StringField(label='מספר המושב שלך:')
    visit_websites = models.StringField(initial="No")
    game_attemptted = models.IntegerField()
    game_correctted = models.IntegerField()
    time_spend = models.StringField()
    price_toSell = models.FloatField()
    first_demo = models.StringField(initial="0")
    first_demo_time = models.StringField()
    second_demo = models.StringField(initial="0")
    second_demo_time = models.StringField()
    demo1_button_sequence = models.StringField()
    demo2_button_sequence = models.StringField()
    #     choices=['18-19', '20-21', '22-23', '24-25', '26 and older'],
    #     label='How old are you',
    #     widget=widgets.RadioSelect)
    # gender = models.StringField(
    #     choices=['Male', 'Female'],
    #     label='What is your gender?',
    #     widget=widgets.RadioSelect)
    # sudokoHobby = models.StringField(
    #     choices=['very much', 'to a great degree', 'in some  ocassions', 'rarely', 'rarely or not at all'],
    #     label='Do you practice Sudoko as a hobby?',
    #     widget=widgets.RadioSelect)
    # wordNumberHobby = models.StringField(
    #     choices=['very much', 'to a great degree', 'in some  ocassions', 'rarely', 'rarely or not at all'],
    #     label='Do you practice “word puzzles” and “number puzzles” as a hobby?',
    #     widget=widgets.RadioSelect)
    age = models.StringField(
        choices=[' 18-19', ' 20-21', ' 22-23', '24-25', '26 ומעלה'],
        label='א.	מהו גילך ',
        widget=widgets.RadioSelect)
    gender = models.StringField(
        choices=['גבר', 'אישה'],
        label='ב.	ציין\ח את מגדרך',
        widget=widgets.RadioSelect)
    sudokoHobby = models.StringField(
        choices=['הרבה פעמים', 'לעתים קרובות', 'מדי פעם', 'באופן נדיר', 'אף פעם לא'],
        label='ג.	האם בעבר פתרת סודוקו כתחביב',
        widget=widgets.RadioSelect)
    wordNumberHobby = models.StringField(
        choices=['הרבה פעמים', 'לעתים קרובות', 'מדי פעם', 'באופן נדיר','אף פעם לא'],
        label='ד.	האם בעבר פתרת משחקי אותיות או מספרים כתחביב',
        widget=widgets.RadioSelect)
    
