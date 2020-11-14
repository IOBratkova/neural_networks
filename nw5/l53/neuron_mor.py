import random
import math

class NeuronMor:
    def __init__(self, count_input, count_output, w_range):
        self.count_input = count_input
        self.count_output = count_output
        self.w_list = [random.uniform(w_range[0], w_range[1]) for _ in range(count_output)]
        self.potential = None
        self.exi = None

    def __str__(self):
        s = 'Нейрон'
        s += ' (\n\t\tвходов = ' + str(self.count_input) + ', '
        s += 'выходов = ' + str(self.count_output) + ', '
        s += '\n\t\tвеса на выходе = ' + str(self.w_list) + ', '
        s += '\n\t\tпотенциалы = ' + str(self.potential) + '\n)'
        return s

    def calc_u_vh(self, x_lst, ws_lst):
        pot = 0.0
        for i in range(len(ws_lst)):
            pot += x_lst[i] * ws_lst[i]
        return pot

    def calc_u_output(self, x, ws_lst=None):
        if ws_lst is None:
            self.potential = x
            self.exi = x
            return self.potential, self.exi
        else:
            potential = self.calc_u_vh(x, ws_lst)
            self.potential = potential
            exi = self.activation_function(potential)
            self.exi = exi
            return potential, exi

    def activation_function(self, p):
        return 1.0 / (1.0 + math.exp(-p))

    def product_activation_function(self, p):
        return self.activation_function(p) * (1 - self.activation_function(p))


