import random
import numpy as n


class Perceptron:
    def __init__(self, count_s, count_a, w_range=(0.1, 0.9)):
        self.s_array = [0 for _ in range(count_s)]
        self.a_array = [0 for _ in range(count_a)]
        self.r = None
        self.s_a_matrix = [[random.uniform(w_range[0], w_range[1]) for _ in range(len(self.s_array))] for _ in range(len(self.a_array))]
        self.a_r_matrix = [random.uniform(w_range[0], w_range[1]) for _ in range(len(self.a_array))]

    def u_input_all_a(self, lst):
        res = []
        for i in range(len(self.a_array)):
            tmp = [lst[j] for j in range(len(self.s_array))]
            result = [tmp[i] for i in range(len(tmp))]
            r = n.sum([lst[j] * self.s_a_matrix[i][j] for j in range(len(self.s_array))])
            res.append(r)
        return res

    def u_input_r(self, lst):
        r = [lst[j] * self.a_r_matrix[j] for j in range(len(self.a_array))]
        return n.sum(r)

    def get_excitatory_neurons(self, letter):
        array = [i for i in range(len(letter)) if letter[i] == 1]
        return array

    def delta_w(self, ny, nak, n, flag):
        return (ny - ((nak*ny)/n)) if flag else (-((nak*ny)/n))








