from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Welcome(Page):
    pass

class Questions(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'sudokoHobby', 'wordNumberHobby']


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
    form_model = 'player'
    form_fields = ['first_demo', 'first_demo_time','second_demo','second_demo_time','demo1_button_sequence','demo2_button_sequence']

class Sudoku(Page):
    form_model = 'player'
    form_fields = ['game_attemptted','game_correctted', 'time_spend','visit_websites']

class Buy(Page):
    form_model = 'player'
    form_fields = ['price_toBuy']


class Result(Page):
    pass

class Result1(Page):
    pass


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
    Result,
    Buy,
    Result1,
]
