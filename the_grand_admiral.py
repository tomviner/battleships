import numpy
import random


class Admiral():

    def __init__(self):
        self.grid = numpy.zeros([10, 10])
        self.lastmove = None
        self.ships = [5, 4, 3, 3, 2]

    def fire(self):
        while True:
            coords = random.choice(range(10)), random.choice(range(10))
            if numpy.isnan(self.grid[coords]):
                break

        self.lastmove = coords
        resp_coords = self.coordToResponse(coords)
        print(resp_coords)
        return resp_coords

    def play(self, resp=None):
        assert resp in ['h', 'm', 's', None]
        self.grid[self.lastmove] = resp
        return self.fire()

    def coordToResponse(self, coords):
        dictionary = {number: letter for letter, number in zip("abcdefghij", range(10))}
        x = dictionary[coords[0]]
        y = coords[1] + 1
        return str(x) + str(y)


def get_random_coord():
    return random.choice(range(10)), random.choice(range(10))


def test_coord_to_response():
    ai = Admiral()
    assert ai.coordToResponse((0, 0)) == "a1", ai.coordToResponse((0, 0))
    assert ai.coordToResponse((9, 9)) == "j10", ai.coordToResponse((9, 9))
    assert ai.coordToResponse((4, 3)) == "e4", ai.coordToResponse((4, 3))
