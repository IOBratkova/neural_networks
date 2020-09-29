import math


class Const(object):

    def __init__(self):
        self.binary_function = ('Бинарная', self.binary)
        self.bipolar_function = ('Биполярная', self.bipolar)

    def bipolar(self, s):
        return 1 if s > 0 else -1

    def binary(self, s):
        return 1 if s > 0 else 0

    # От 0 до 1
    def sigmoid(self, s):
        return 1 / (1 + math.pow(math.e, -s))

    # От -1 до 1
    def tanh(self, s):
        return 2 / (1 + math.pow(math.e, -2 * s)) - 1

    def re_lu(self, s):
        return max(0, s)
