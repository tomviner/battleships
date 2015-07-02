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

class AI_but_no_repeat(object):
    def __init__(self):
        self.done = set()

    def play(self, previous_result=None):
        while 1:
            mv = get_random_coord()
            if mv in self.done:
                continue
            self.done.add(mv)
            return mv
