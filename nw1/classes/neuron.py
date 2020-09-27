class Neuron:
    def __init__(self, count_input, count_output, function):
        self.count_input = count_input
        self.count_output = count_output
        self.w_list = []
        self.function = function

