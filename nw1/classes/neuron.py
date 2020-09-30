class Neuron:
    def __init__(self, count_input, count_output, x_list, function):
        self.count_input = count_input
        self.count_output = count_output
        self.x_list = x_list  # нахуа он мне
        self.w_list = [0 for _ in range(count_input)]
        self.function = function

    def z(self, b):
        z = 0
        i = 0
        while i < self.count_input:
            z += self.x_list * self.w_list
        return z + b

    def correction_w_list(self, x, y):
        for w in self.w_list:
            res = self.__correction_w(w, x, y)

    def __correction_w(self, w, x, y):
        return self.function[2](w, x, y)
