import csv

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'sudoku'
    players_per_group = None
    num_rounds = 1
    with open('sudoku/game.csv') as questions_file:
        playList = list(csv.reader(questions_file))

    num_rounds = len(playList)


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number ==1:
            self.session.vars['games'] = Constants.playList.copy()
        for p in self.get_players():
            game_data = p.current_games()
            p.game_id = int(game_data[self.round_number])
            p.answer = int(game_data[self.round_number])



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    game_id = models.IntegerField()
    question_id = models.IntegerField()
    game_attempt = models.IntegerField(initial=0)
    game_correct = models.IntegerField(initial=0)
    answer = models.IntegerField()


    def current_games(self):
        return self.session.vars['games'][self.round_number - 1]

    def attempt_more(self):
        self.game_attempt += 1

    def correct(self):
        self.game_correct += 1

    def convertInt(self, inte):
        if inte == 'A':
            return 0
        elif inte == 'B':
            return 1
        elif inte == 'C':
            return 2
        elif inte == 'D':
            return 3
