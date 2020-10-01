# Функции переехали сюда
# from math import pow, e
# function_dict = {'Биполярная': (lambda x: 1 if x > 0 else 0, lambda w, x, y: w + 1 if x == 1 and y == 1 else
# w - 1 if x != 0 and not y else w if not x else w),
#                       'Бинарная': (lambda x: 1 if x > 0 else -1, lambda w, x, y: w + x * y)}
# functions_s = [lambda s: 1 / (1 + pow(e, -s)), lambda s: 2 / (1 + pow(e, -2 * s)) - 1, lambda s: max(0, s)]
import math



class ActivationFunctionConst(object):

    def __init__(self):
        self.binary_function = ('Бинарная', self.binary, self.hebb_for_binary)
        self.bipolar_function = ('Биполярная', self.bipolar, self.hebb_for_bipolar)

    def bipolar(self, s, div):
        return (1, 'A') if s > div else (-1, 'B')

    def hebb_for_bipolar(self, w, x, y):
        return w + x * y

    def binary(self, s, div):
        return (1, 'A') if s > div else (0, 'B')

    def hebb_for_binary(self, w, x, y):
        delta_w = 0
        if x == 1 and y == 1:
            delta_w = 1
        elif x == 0:
            delta_w = 0
        elif x != 0 and y == 0:
            delta_w = -1
        return w + delta_w

    # От 0 до 1
    def sigmoid(self, s):
        return 1 / (1 + math.pow(math.e, -s))

    # От -1 до 1
    def tanh(self, s):
        return 2 / (1 + math.pow(math.e, -2 * s)) - 1

    def re_lu(self, s):
        return max(0, s)
