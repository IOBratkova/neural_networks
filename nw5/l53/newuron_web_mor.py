from l53.neuron_mor import NeuronMor
import copy
import math


class NeuronWebMor:
    def __init__(self, count_input_neurons, count_output, count_hide_layers,
                 w_range=(-0.5, 0.5)):  # входных, выходнх, средних слоев

        self.count_input_neurons = count_input_neurons
        self.count_output_neurons = count_output
        self.count_hide_layers = count_hide_layers

        self.count_neurons_in_hide, self.hide_neurons = self.__make_neurons_in_hide__(count_input_neurons, count_hide_layers, count_output, w_range)


        self.input_neurons = [
            NeuronMor(1, self.count_neurons_in_hide[0], w_range) for _ in range(count_input_neurons)
        ]

        self.output_neurons = [
            NeuronMor(len(self.hide_neurons[-1]), 1, w_range) for _ in range(count_output)
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

    def __make_neurons_in_hide__(self, count_input, count_hide_layers, count_output, w_range):
        def __calc_count():
            if count_input > 8:
                res = []
                first = int(count_input / 2)
                lastt = int(count_input / 4)
                for i in range(count_hide_layers):  # по количеству слоёв
                    if i == 0:
                        res.append(first)
                    elif i == count_hide_layers - 1:
                        res.append(lastt)
                    else:
                        first2 = res[i - 1] - 2
                        t = first2 if first2 > lastt else lastt
                        res.append(t)
                return res
            else:
                return [2, 2]

        def __make_neurons():
            res = []
            length = len(count_hide_neurons)
            for i in range(length):
                if i == 0:
                    t = [NeuronMor(count_input, count_hide_neurons[i + 1], w_range) for _ in
                         range(count_hide_neurons[i])]
                    res.append(t)
                elif i == length - 1:
                    t = [NeuronMor(count_hide_neurons[i - 1], count_output, w_range) for _ in
                         range(count_hide_neurons[i])]
                    res.append(t)
                else:
                    t = [NeuronMor(count_hide_neurons[i - 1], count_hide_neurons[i + 1], w_range) for _ in
                         range(count_hide_neurons[i])]
                    res.append(t)
            return res

        count_hide_neurons = __calc_count()
        return count_hide_neurons, __make_neurons()

    def teaching(self, patterns, ny):
        self.list_patterns = patterns
        indexes = [i for i in range(len(patterns))]
        count_epoch = 0
        flag = False
        while not flag:
            exis = []
            for i in range(len(patterns)):
                if i in indexes:
                    self.direct_way(patterns[i][0])
                    self.reverse_way(patterns[i][1])
                    self.error_correct(ny)
                    # exi = copy.copy([e.exi for e in self.output_neurons])
                    exi = patterns[i][1]
                    exis.append(exi)

            flag, indexes = self.__ost(patterns, exis, indexes)
            count_epoch += 1
        print('\nПотребовалось эпох: '+str(count_epoch))
        for o in self.output_neurons:
            print(o)

    def recognize(self, letter):
        self.direct_way(letter)
        exi = [e.exi for e in self.output_neurons]
        print('Выходы: ')
        print(exi)

    def __ost(self, patterns, exis1, last_idexes, eps=0.1):
        exis2 = []
        for i in range(len(patterns)):
            if i in last_idexes:
                self.direct_way(patterns[i][0])
                exi2 = copy.copy([e.exi for e in self.output_neurons])
                exis2.append(exi2)

        indexes = []
        for i in range(len(exis2)):
            e1 = exis1[i]
            e2 = exis2[i]
            for j in range(len(e2)):
                if math.fabs(e1[j] - e2[j]) < eps:
                    continue
                else:
                    if i not in indexes:
                        indexes.append(i)
        return (False, indexes) if len(indexes) != 0 else (True, [])


        # for i in range(len(exi2)):


        # for i in range(epoch):
        #     #print('Эпоха №' + str(i+1))
        #     for pattern in patterns:
        #         self.direct_way(pattern[0])
        #         self.reverse_way(pattern[1])
        #         self.error_correct(ny)
        # print('end')
        #
        # print(self.output_neurons[0])
        # #ripnt(self.__str__())

    def direct_way(self, pattern):
        for i in range(self.count_input_neurons):
            self.input_neurons[i].calc_u_output(pattern[i])

        potentials = [neuron.exi for neuron in self.input_neurons]
        for i in range(len(self.hide_neurons[0])):
            ws_lst = [n.w_list[i] for n in self.input_neurons]
            self.hide_neurons[0][i].calc_u_output(potentials, ws_lst)

        potentials = [neuron.exi for neuron in self.hide_neurons[0]]
        for i in range(1, self.count_hide_layers):
            for j in range(len(self.hide_neurons[i])):
                ws_lst = [n.w_list[j] for n in self.hide_neurons[i - 1]]
                self.hide_neurons[i][j].calc_u_output(potentials, ws_lst)

        potentials = [neuron.exi for neuron in self.hide_neurons[-1]]
        for i in range(self.count_output_neurons):
            ws_lst = [n.w_list[i] for n in self.hide_neurons[-1]]
            self.output_neurons[i].calc_u_output(potentials, ws_lst)

    def reverse_way(self, pattern):
        for i in range(self.count_output_neurons):
            self.output_neurons[i].calc_error_signal(pattern[i])

        for i in range(len(self.hide_neurons[-1])):
            self.hide_neurons[-1][i].calc_error_signal(self.output_neurons)

        for i in range(0, self.count_hide_layers - 1):
            for j in range(len(self.hide_neurons[i])):
                self.hide_neurons[i][j].calc_error_signal(self.hide_neurons[i + 1])

    def error_correct(self, ny=0.5):
        for i in range(self.count_input_neurons):
            self.input_neurons[i].ws_correction(ny, self.hide_neurons[0])

        for i in range(0, self.count_hide_layers - 1):
            for j in range(len(self.hide_neurons[i])):
                self.hide_neurons[i][j].ws_correction(ny, self.hide_neurons[i+1])

        for i in range(len(self.hide_neurons[-1])):
            self.hide_neurons[-1][i].ws_correction(ny, self.output_neurons)

        # for i in range(self.count_output_neurons):
        #     self.output_neurons[i].ws_correction(ny, self.output_neurons)
