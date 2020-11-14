import math
import random


class NeuronMor:
    def __init__(self, count_inp, count_out, w_range):
        self.count_inp = count_inp
        self.input_ws = \
            [random.uniform(w_range[0], w_range[1]) for _ in range(count_out)]

    # def activation_function(self, p):
    #     return 1.0/(1.0 + math.exp(-p))
    #
    # def product_activation_function(self, p):
    #     return self.activation_function(p) * (1 - self.activation_function(p))