from l53.neuron_mor import NeuronMor


class NeuronWebMor:
    def __init__(self, count_input_neurons, count_output, count_hide_layers, w_range=(-0.5, 0.5)): #входных, выходнх, средних слоев
        self.count_input_neurons = count_input_neurons
        self.count_output_neurons = count_output
        self.count_hide_layers = count_hide_layers
        self.count_neurons_in_hide = \
            self.__make_count_neurons_in_hide__(count_input_neurons, count_hide_layers)
        self.hide_neurons = \
            self.__make_hide_neurons__(self.count_neurons_in_hide, count_input_neurons, count_output, w_range)
        self.input_neurons = [
            NeuronMor(1, self.count_neurons_in_hide[0], w_range) for _ in range(count_input_neurons)
        ]
        self.output_neurons = [
            NeuronMor(len(self.hide_neurons[-1]), 1, (0.0, 0.0)) for _ in range(count_output)
        ]
        self.list_patterns = None

    def __str__(self):
        def __lst_neurons_to_string(lst, tab='\t'):
            s = ''
            for l in range(len(lst)):
                k = l + 1
                if l == len(lst) - 1:
                    s += tab + str(k) + '-' + str(lst[l])
                else:
                    s += tab + str(k) + '-' + str(lst[l]) + '\n'
            return s

        def __matrix_neurons_to_string(matrix):
            s = ''
            for m in range(len(matrix)):
                k = m + 1
                if m == len(matrix) - 1:
                    s += '\n\tСлой №' + str(k) + '\n' + __lst_neurons_to_string(matrix[m], '\t\t')
                else:
                    s += '\n\tСлой №' + str(k) + '\n' + __lst_neurons_to_string(matrix[m], '\t\t') + '\n'
            return s

        s = 'Сеть.\nВходной слой = {\n'

        t = __lst_neurons_to_string(self.input_neurons)
        s += str(t) + '\n}\n'

        s += '\nСкрытые слои = {\n'
        t = __matrix_neurons_to_string(self.hide_neurons)
        s += str(t) + '\n}\n'

        s += '\nВыходной слой = {\n'
        t = __lst_neurons_to_string(self.output_neurons)
        s += str(t) + '\n}\n'
        return s

    def teaching(self, patterns):
        self.list_patterns = patterns

    def direct_way(self):


    def __make_count_neurons_in_hide__(self, count_input_neurons, count_hide_layers):
        res = []

        first = int(count_input_neurons / 2)
        lastt = int(count_input_neurons / 4)

        for i in range(count_hide_layers): #по количеству слоёв
            if i == 0:
                res.append(first)
            elif i == count_hide_layers - 1:
                res.append(lastt)
            else:
                first2 = res[i-1] - 2
                t = first2 if first2 > lastt else lastt
                res.append(t)
        return res

    def __make_hide_neurons__(self, count_hide_neurons, count_input, count_output, w_range):
        res = []

        length = len(count_hide_neurons)

        for i in range(length):
            if i == 0:
                t = [NeuronMor(count_input, count_hide_neurons[i + 1], w_range) for _ in range(count_hide_neurons[i])]
                res.append(t)
            elif i == length - 1:
                t = [NeuronMor(count_hide_neurons[i - 1], count_output, w_range) for _ in range(count_hide_neurons[i])]
                res.append(t)
            else:
                t = [NeuronMor(count_hide_neurons[i - 1], count_hide_neurons[i + 1], w_range) for _ in range(count_hide_neurons[i])]
                res.append(t)
        return res






