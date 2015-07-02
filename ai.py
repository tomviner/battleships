import random

along = 'ABCDEFGHIJ'
down = range(1, 11)

def get_random_coord():
    a = random.choice(along)
    d = random.choice(down)
    return '{}{}'.format(a, d)

class AI(object):
    def play(self, previous_result=None):
        return get_random_coord()
