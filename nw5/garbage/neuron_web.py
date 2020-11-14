from garbage.mor_neuron import NeuronMor

class NeuronWeb:
    def __init__(self, count_inp, count_hid, count_out, w_range):
        self.count_input_layer = count_inp # Входные нейроны
        self.count_hide_layers = count_hid # Скрытые слои
        self.count_output_layers = count_out #Выходной слой

        self.output_list = [
            NeuronMor(count_out, 1, w_range) for i in range(count_out)
        ]
        self.hide_lists = [[]]
        self.input_list = [
            NeuronMor(1, )
        ]


