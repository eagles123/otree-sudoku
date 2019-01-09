from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class InputId(Page):
    form_model ="player"
    form_fields = ["subject_id"]

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

class Instruction7(Page):
    pass

class DemoGame(Page):
    form_model = 'player'
    form_fields = ['first_demo', 'first_demo_time','second_demo','second_demo_time','demo1_button_sequence','demo2_button_sequence']

class Sudoku(Page):
    form_model = 'player'
    form_fields = ['game_attempted_seriously', 'games_looked_at', 'game_correctted', 'time_spend', 'skip_time', 'visit_websites']

class Buy(Page):
    form_model = 'player'
    form_fields = ['price_toBuy']


class Result(Page):
    def vars_for_template(self):
        return {'game_attempped' : self.player.game_attempted_seriously + self.player.games_looked_at}

class Result1(Page):
    pass


page_sequence = [
    # InputId,
    # Welcome,
    # Questions,
    # Award,
    # Instruction2,
    # Instruction3,
    # Instruction4,
    # DemoGame,
    # Instruction5,
    # Instruction6,
    # Instruction7,
    Sudoku,
    Result,
    Buy,
    Result1,
]
