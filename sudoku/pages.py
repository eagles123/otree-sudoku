from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'experience']


class Award(Page):
    pass

class Instruction2(Page):
    pass

class Instruction3(Page):
    pass

class Instruction4(Page):
    pass
class Instruction5(Page):
    pass

class Instruction6(Page):
    pass

class Seat(Page):
    form_model = 'player'
    form_fields = ['seat_number']


class Instruction7(Page):
    pass

class DemoGame(Page):
    pass

class Sudoku(Page):
    form_model = 'player'
    form_fields = ['game_attemptted','game_correctted', 'time_spend', 'is_terminated']

class Buy(Page):
    form_model = 'player'
    form_fields = ['price_toBuy']
    def is_displayed(self):
        return self.player.is_terminated == "No"

class Stop(Page):
    def is_displayed(self):
        return self.player.is_terminated == "Yes"

class Result1(Page):
    def is_displayed(self):
        return self.player.is_terminated == "NO"



page_sequence = [
    Welcome,
    # Questions,
    # Award,
    # Instruction2,
    # Instruction3,
    # Instruction4,
    # DemoGame,
    # Seat,
    # Instruction5,
    # Instruction6,
    # Instruction7,
    Sudoku,
    Buy,
    Result1,
    Stop,
]
