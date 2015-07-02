# import sys
import random
from ai import AI


class GameRunner(object):
    """GameRunner"""
    def __init__(self):
        self.board = {
            'A1': 'x',
            'A2': 'x',
            'A3': 'x',
        }

    def run(self):
        a = AI()
        coords = a.play()
        print coords
        while self.board:
            result = random.choice('hms')
            print result
            coords = a.play(result)
            if coords in self.board:
                result = 'h'
                del self.board[coords]
            print
        print('game over!')


gr = GameRunner()
gr.run()
