from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    pass

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



class Results(Page):
    pass



page_sequence = [
    Instruction,
    Sudoku,
    Results
]
