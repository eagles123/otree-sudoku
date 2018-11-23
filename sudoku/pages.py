from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    def is_displayed(self):
        return self.round_number == 1

class Questions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'experience']
    def is_displayed(self):
        return self.round_number == 1

class Award(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruction2(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruction3(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruction4(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruction5(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruction6(Page):
    def is_displayed(self):
        return self.round_number == 1

class Seat(Page):
    form_model = 'player'
    form_fields = ['seat_number']
    def is_displayed(self):
        return self.round_number == 1

class Start(Page):
    def is_displayed(self):
        return self.round_number == 1

class Sudoku(Page):
    form_model = 'player'

    def vars_for_template(self):
        grid = []
        game = self.player.current_games()
        for i in range(4):
            grid.append(game[4 * i:4 * (i + 1)])
        data = {}
        for i in 'ABCD':
            for j in '1234':
                data[i + j] = grid[self.player.convertInt(i)][int(j) - 1]
        return data

    def before_next_page(self):
        for i in 'ABCD':
            for j in '1234':
                print(self.vars_for_template()[i+j])



class Results(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds



page_sequence = [
    Welcome,
    Questions,
    Award,
    Instruction2,
    Instruction3,
    Instruction4,
    Instruction5,
    Instruction6,
    Seat,
    Start,
    Sudoku,
    Results
]
