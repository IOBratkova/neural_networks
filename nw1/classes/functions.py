import math


class ActivationFunctionConst(object):

    def __init__(self):
        self.binary_function = ('Бинарная', self.binary, self.hebb_for_binary)
        self.bipolar_function = ('Биполярная', self.bipolar, self.hebb_for_bipolar)
        self.sigmoid_function = ('Сигмоидальная', self.sigmoid, self.hebb_for_binary)

    def sigmoid(self, s, t):
        return 1 / (1 + math.pow(math.e, -t*s))

    def bipolar(self, s, div):
        return (1, 'A') if s > div else (-1, 'B')

    def hebb_for_bipolar(self, w, x, y, k=1.0):
        return w + x * y * k

    def binary(self, s, div):
        return (1, 'A') if s > div else (0, 'B')

    def hebb_for_binary(self, w, x, y, k=1.0):
        delta_w = 0
        if x == 1 and y == 1: delta_w = 1
        elif x == 0: delta_w = 0
        elif x != 0 and y == 0: delta_w = -1
        return w + delta_w * k


    #
    # # От -1 до 1
    # def tanh(self, s):
    #     return 2 / (1 + math.pow(math.e, -2 * s)) - 1
    #
    # def re_lu(self, s):
    #     return max(0, s)
