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
    name_in_url = 'sudoku'
    players_per_group = None
    num_rounds = 1
    fixed_price = 15


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    seat_number = models.StringField(label='Your Seat Number:')
    game_attemptted = models.IntegerField()
    game_correctted = models.IntegerField()
    is_terminated = models.StringField()
    time_spend = models.StringField()
    price_toBuy = models.FloatField()
    age = models.StringField(
        choices=['18-19', '20-21', '22-23', '24-25', '26 and older'],
        label='How old are you',
        widget=widgets.RadioSelect)
    gender = models.StringField(
        choices=['Male', 'Female'],
        label='What is your gender?',
        widget=widgets.RadioSelect)
    experience = models.StringField(
        choices=['very much', 'to a great degree', 'in some  ocassions', 'rarely or not at all'],
        label='Do you practice “word puzzles” and “number puzzles” as a hobby,',
        widget=widgets.RadioSelect)