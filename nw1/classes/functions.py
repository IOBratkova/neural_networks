import math


def make_ladder(q1, q2, k):
    dq = (q2 - q1) / (k - 1)
    q_list = []
    for i in range(1, k):
        q_list.append(q1 + (i - 1) * dq)
    return q_list


class ActivationFunctionConst(object):

    def __init__(self):
        self.binary_function = ('Бинарная', self.binary, self.hebb_for_binary)
        self.bipolar_function = ('Биполярная', self.bipolar, self.hebb_for_bipolar)
        self.sigmoid_function = ('Сигмоидальная', self.sigmoid, self.hebb_for_binary)
        self.ladder_binary_function = ('Ступенчатая бинарная', self.binary_ladder, self.binary)

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

    def binary_ladder(self, q_list, k, s):
        if s < q_list[0]:
            return 0
        if s >= q_list[len(q_list) - 1]:
            return 1
        for i in range(1, len(q_list)):
            if q_list[i] >= s >= q_list[i - 1]:
                return i / (k - 1)
    #
    # # От -1 до 1
    # def tanh(self, s):
    #     return 2 / (1 + math.pow(math.e, -2 * s)) - 1
    #
    # def re_lu(self, s):
    #     return max(0, s)
