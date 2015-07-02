# import sys
import time
from ai import AI, get_random_coord


class GameRunner(object):
    """GameRunner
    {
        'A1': 'x',
        'A2': 'x',
        'A3': 'x',
    }
    """
    def __init__(self):
        self.board = {}
        for l, ship in zip((5, 4, 3, 3, 2), 'vwxyz'):
            coords = get_random_coord()
            self.board[coords] = ship

    def run(self):
        a = AI()
        result = None
        moves = 0
        while self.board:
            moves += 1
            print result
            print
            print
            time.sleep(0.01)
            coords = a.play(result)
            print coords
            if coords in self.board:
                result = 'h'
                ships_before = set(self.board.values())
                del self.board[coords]
                ships_after = set(self.board.values())
                diff = ships_before - ships_after
                if diff:
                    sunk = diff.pop()
                    print 'sunk', sunk
                    result = 's'
                else:
                    print 'h'
            else:
                result = 'm'
            print self.board
        print('game over! in {} moves'.format(moves))


gr = GameRunner()
gr.run()
