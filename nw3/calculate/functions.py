import math


class ActivationFunctionConst(object):

    def __init__(self):
        self.binary_function = ('Бинарная', self.binary, self.hebb_for_binary, (1, 0))
        self.bipolar_function = ('Биполярная', self.bipolar, self.hebb_for_bipolar, (1, -1))
        self.sigmoid_function = ('Сигмоидальная', self.sigmoid, self.hebb_for_binary, (1, 0))
        self.bipolar_delta_function = ('D-правило, биполяр.', self.bipolar, self.delta_for_bipolar, (1, -1))
        self.functions_list = [self.binary_function, self.bipolar_function,  self.sigmoid_function, self.bipolar_delta_function]

    def bipolar(self, s, div):
        return 1 if s > div else -1

    def hebb_for_bipolar(self, w, x, y, k=1.0):
        return w + x * y * k

    def delta_for_bipolar(self, w_old, u_in, u_out, x, alpha=0.1):
        return w_old + alpha * (u_out - u_in) * x

    def sigmoid(self, s, t):
        return 1 / (1 + math.pow(math.e, -t*s))

    def binary(self, s, div):
        return 1 if s > div else 0

    def hebb_for_binary(self, w, x, y, k=1.0):
        delta_w = 0
        if x == 1 and y == 1: delta_w = 1
        elif x == 0: delta_w = 0
        elif x != 0 and y == 0: delta_w = -1
        return w + delta_w * k
