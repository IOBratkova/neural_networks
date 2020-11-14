import random
import math

class NeuronMor:
    def __init__(self, count_input, count_output, w_range):
        self.count_input = count_input
        self.count_output = count_output
        self.w_list = [random.uniform(w_range[0], w_range[1]) for _ in range(count_output)]
        self.potential = None

    def __str__(self):
        s = 'Нейрон'
        s += '(входов = ' + str(self.count_input) + ', '
        s += 'выходов = ' + str(self.count_output) + ', '
        s += '\n\t\t\t\tвеса на выходе = ' + str(self.w_list) + ', '
        s += '\n\t\t\t\tпотенциалы = ' + str(self.potential) + ')'
        return s

    # def u_vh(self):
    #     res =

    def cal_potential(self, x_lst, ws_lst):
        pot = 0.0
        for i in range(self.count_input):
            pot += x_lst[i] * ws_lst[i]
        return pot

    def calc_u_otput(self, x_lst, ws_lst):
        potential = self.cal_potential(x_lst, ws_lst)

    def activation_function(self, p):
        return 1.0 / (1.0 + math.exp(-p))

    def product_activation_function(self, p):
        return self.activation_function(p) * (1 - self.activation_function(p))


