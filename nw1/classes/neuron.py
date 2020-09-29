class Neuron:
    def __init__(self, count_input, count_output, x_list, function):
        self.count_input = count_input
        self.count_output = count_output
        self.x_list = x_list
        self.w_list = [0 for i in range(count_input)]
        self.function = function

    # входоной суммарный сигнал (s)
    def z(self, b):
        z = 0
        i = 0
        while i < self.count_input:
            z += self.x_list * self.w_list
        return z + b

