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

    # with open('sudoku/game.csv') as questions_file:
    #     playList = list(csv.reader(questions_file))
    #
    # num_rounds = len(playList


class Subsession(BaseSubsession):
    pass
    # def creating_session(self):
    #     if self.round_number ==1:
    #         self.session.vars['games'] = Constants.playList.copy()
    #     for p in self.get_players():
    #         game_data = p.current_games()
    #         p.game_id = int(game_data[self.round_number])
    #         p.answer = int(game_data[self.round_number])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    seat_number = models.StringField(label='Your Seat Number:')
    game_attemptted = models.IntegerField()
    game_correctted = models.IntegerField()
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


    # def current_games(self):
    #     return self.session.vars['games'][self.round_number - 1]
    #
    # def attempt_more(self):
    #     self.game_attempt += 1
    #
    # def correct(self):
    #     self.game_correct += 1
    #
    # def convertInt(self, inte):
    #     if inte == 'A':
    #         return 0
    #     elif inte == 'B':
    #         return 1
    #     elif inte == 'C':
    #         return 2
    #     elif inte == 'D':
    #         return 3
