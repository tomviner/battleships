from __future__ import division
import random
import time
from the_grand_admiral import Admiral as AI, get_random_coord

class InvalidShipError(ValueError):
    pass

class GameRunner(object):
    """GameRunner
    {
        'A1': 'x',
        'A2': 'x',
        'A3': 'x',
    }
    """
    def __init__(self, DEBUG=False):
        self.DEBUG = DEBUG
        self.board = {}
        for n, ship_name in zip((5, 4, 3, 3, 2), 'vwxyz'):
            valid = False
            while not valid:
                try:
                    tmp_board = {}
                    for i in range(n):
                        if i == 0:
                            ship_coords = []
                            coords = get_random_coord()
                            is_horizontal = random.choice((False, True))
                        else:
                            last_coord = ship_coords[-1]
                            print(last_coord)
                            letter = last_coord[0]
                            number = last_coord[1:]
                            if is_horizontal:
                                letter = chr(ord(letter) + 1)
                                if letter == 'K':
                                    raise InvalidShipError
                            else:
                                number = int(number)
                                number += 1
                                if number > 10:
                                    raise InvalidShipError
                            coords = '{}{}'.format(letter, number)
                        if coords in self.board:
                            raise InvalidShipError
                        tmp_board[coords] = ship_name
                        ship_coords.append(coords)
                except InvalidShipError:
                    continue
                else:
                    self.board.update(tmp_board)
                    break

    def print_board(self):
        for letter in 'ABCDEFGHIJ':
            for number in range(1, 11):
                coords = '{}{}'.format(letter, number)
                print(self.board.get(coords, '.'), end=' ')

            print(' ', end='\n')

    def run(self):
        a = AI()
        result = None
        moves = 0
        while self.board:
            moves += 1
            print(result)
            self.print_board()
            print()
            print()
            if self.DEBUG:
                time.sleep(1)
            coords = a.play(result)
            print(coords)
            if coords in self.board:
                result = 'h'
                ships_before = set(self.board.values())
                del self.board[coords]
                ships_after = set(self.board.values())
                diff = ships_before - ships_after
                if diff:
                    sunk = diff.pop()
                    print('sunk', sunk)
                    result = 's'
                else:
                    print('h')
            else:
                result = 'm'
            print(self.board)
        print('game over! in {} moves'.format(moves))
        return moves


av = lambda ns: sum(ns) / len(ns)
results = []
for i in range(10):
    gr = GameRunner()
    results.append(gr.run())
print(results, av(results))
