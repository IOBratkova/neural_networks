import random
import numpy
import copy
import math


class Perceptron:
    def __init__(self, count_s, count_a, w_range=(0.1, 0.9)):
        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.s_array = [0 for _ in range(count_s)]
        self.a_array = [0 for _ in range(count_a)]
        self.r = None
        self.s_a_matrix = [[random.uniform(w_range[0], w_range[1]) for _ in range(len(self.s_array))] for _ in range(len(self.a_array))] #[[0.1 if i % 2 == 0 else 0.5 for i in range(len(self.s_array))] for _ in range(len(self.a_array))]
            # [[0.3, 0.2, 0.1, 0.6, 0.5, 0.4, 0.9, 0.6, 0.7],
            #                [0.2, 0.1, 0.3, 0.4, 0.5, 0.6, 0.7, 0.1, 0.9],
            #                [0.3, 0.5, 0.1, 0.6, 0.3, 0.4, 0.9, 0.4, 0.7], #пятый зменен с 0.3 на 0.5
            #                [0.4, 0.3, 0.2, 0.1, 0.8, 0.7, 0.6, 0.6, 0.9],
            #                [0.5, 0.3, 0.3, 0.6, 0.1, 0.2, 0.9, 0.2, 0.7],
            #                [0.6, 0.5, 0.4, 0.1, 0.2, 0.3, 0.8, 0.5, 0.8]
            #                ]

        self.a_r_matrix =[random.uniform(w_range[0], w_range[1]) for _ in range(len(self.a_array))] #[0.1 if i % 2 == 0 else 0.2 for i in range(len(self.a_array))]
            # [0.2, 0.8, 0.6, 0.9, 0.8, 0.1]


    def u_input_all_a(self, lst):
        # tmp = [lst[j] * self.s_a_matrix[i][j] for j in range(len(self.s_array))]
        res = []
        for i in range(len(self.a_array)):
            ts = []
            for j in range(len(self.s_array)):
                t = lst[j] * self.s_a_matrix[i][j]
                ts.append(round(t, 1))
            r = numpy.sum(ts)
            res.append(round(r, 1))
        return res

    def u_input_r(self, lst):
        r = [lst[j] * self.a_r_matrix[j] for j in range(len(self.a_array))]
        return numpy.sum(r)

    def get_excitatory_neurons(self, letter):
        array = [i for i in range(len(letter)) if letter[i] == 1]
        return array

    def delta_w(self, ny, nak, n, flag):
        return (ny - (nak * ny / n)) if flag else -(nak*ny/n)


    def gamma_correction(self, uvh_array, nyt, element, teta):
        current_w = copy.copy(self.a_r_matrix)
        uvr1 = uvh_array[0]
        uvr2 = uvh_array[1]

        tmp_elem = []
        tmp_elem.append(element[0])
        tmp_elem.append([0 if v == 1 else 1 for v in element[1]])
        summuvr = uvr1 + uvr2
        s = 'UвхR = ' + str(uvh_array) + '\n'
        s += 'Начальные веса: ' + str(current_w) + '\n'
        s += 'Сумма UвхR = ' + str(summuvr) + '\n'
        print(s)
        l = 0
        flag = False
        while not flag:
            k = l + 1
            print('t' + str(k).translate(self.SUB) + ':\n')
            activ = self.select_element(teta, uvh_array, l)
            #tmp = [0 if el == 1 else 1 for el in element[activ]]
            if activ is None:
                print('канец')
                return
            self.calc_Ilia(tmp_elem[activ], self.a_r_matrix, nyt) # tmp =>> element[activ]
            #uvh_array[activ] = self.u_input_r(element[activ])
            uvh_array = [self.u_input_r(element[i]) for i in range(len(element))]
            s = 'Сумма UвхR = ' + str(numpy.sum(self.a_r_matrix)) + '\n'
            print(s)
            l += 1

    def gamma_correction2(self, uvh_array, nyt, element, teta):
        current_w = copy.copy(self.a_r_matrix)
        uvr1 = uvh_array[0]
        uvr2 = uvh_array[1]
        summuvr = uvr1 + uvr2
        s = 'UвхR = ' + str(uvh_array) + '\n'
        s += 'Начальные веса: ' + str(current_w) + '\n'
        s += 'Сумма UвхR = ' + str(summuvr) + '\n'
        print(s)
        l = 0
        flag = False
        not_update_w = []

        while not flag:
            k = l + 1
            print('t' + str(k).translate(self.SUB) + ':\n')
            activ = self.select_element(teta, uvh_array, l)
            if activ is None:
                print('канец')
                return
            current_w, not_update_w = self.calc_dw(element[activ], nyt, not_update_w, current_w)
            #current_w = [current_w[i] + dw[i] for i in range(len(current_w))]
            self.a_r_matrix = current_w
            # self.calc_Ilia(element[activ], self.a_r_matrix, nyt)
            uvh_array[activ] = self.u_input_r(element[activ])
            #uvh_array = [self.u_input_r(element[i]) for i in range(len(element))]
            s = 'Сумма UвхR = ' + str(numpy.sum(self.a_r_matrix)) + '\n'
            print(s)
            l += 1

    def select_element(self, teta, uvh, l):
        if uvh[1] < teta <= uvh[0]:
        #if uvh[1] < uvh[0]:
            return None
        if uvh[1] < teta:
            return 0
        elif uvh[0] >= teta:
            return 1
        else:
            return 0 if l % 2 == 0 else 1

    @staticmethod
    def calc_Ilia(list_activion, list_weight, nya):
        active = []
        passive = []
        for i in range(len(list_activion)):
            if list_activion[i] == 1:
                active.append(i)
            else:
                passive.append(i)
        dw = nya
        eps = 1e-7
        count = 0
        for i in range(len(list_weight)):
            w = list_weight[i]
            if abs(w - 1) < eps and i in active:
                active.remove(i)
                continue
            if abs(w - 0) < eps and i in passive:
                passive.remove(i)
                continue
            max_dw = 1 - w if i in active else w
            if dw > max_dw:
                dw = max_dw
                if i in active:
                    count = len(passive)
                else:
                    count = len(active)
        if count != 0:
            dw *= len(list_activion) / count

        for index in active:
            list_weight[index] += dw * len(passive) / len(list_activion)

        for index in passive:
            list_weight[index] -= dw * len(active) / (len(list_activion))

    def calc_dw(self, index_array, ny, not_update_w, current_w):
        dw_array = []
        lent = len(self.a_r_matrix)
        active = []
        passive = []
        for i in range(len(index_array)):
            if index_array[i] == 1:
                active.append(i)
            else:
                passive.append(i)
        n = len(index_array)
        nak = len(active)
        i = 0
        dw = -self.delta_w(ny, nak, n, True) if i in index_array else self.delta_w(ny, nak, n, False)
        dw, fl = self.help_calc_delta_w(self.a_r_matrix[0], dw)
        func = self.delta_w
        if fl:
            func = self.delta_w_with_flag
            not_update_w.append(i)
        dw_array.append(dw)
        i += 1
        while i < lent:
            fl = False
            if i not in not_update_w:
                dw = -func(ny, nak, n, True) if i in index_array else func(ny, nak, n, False)
                ch, fl = self.help_calc_delta_w(self.a_r_matrix[i], dw)
                dw = ch
            if fl:
                not_update_w.append(i)
                func = self.delta_w_with_flag
            dw_array.append(dw)
            i += 1

        for index in active:
            current_w[index] += dw * len(passive) / (len(current_w))

        for index in passive:
            current_w[index] -= dw * len(active) / (len(current_w))

        return current_w, not_update_w

    # Вернет разность и значение Тистина, если нужно юзать с этого моммента другой способ вычислений
    def help_calc_delta_w(self, w_last, dw_current):
        tmp = 1 - w_last
        tmp2 = numpy.abs(dw_current - w_last)
        if dw_current > tmp:
            return (tmp2, True)
        else:
            return (dw_current, False)
        #return (tmp2, True) if dw_current > tmp else (dw_current, False)

    def gamma_correction3(self, uvh_array, nyt, element, teta):
        current_w = copy.copy(self.a_r_matrix)
        current_w = [round(c, 2) for c in current_w]
        uvr1 = uvh_array[0]
        uvr2 = uvh_array[1]
        summuvr = uvr1 + uvr2
        s = 'UвхR = ' + str(uvh_array) + '\n'
        s += 'Начальные веса: ' + str(current_w) + '\n'
        s += 'Сумма UвхR = ' + str(summuvr) + '\n'
        print(s)
        l = 0
        flag = False
        not_update_w0 = []
        while not flag:
            k = l + 1
            print('t' + str(k).translate(self.SUB) + ':\n')
            activ = self.select_element(teta, uvh_array, l)
            if activ is None:
                print('канец')
                return
            tmp, tmp2 = self.calculate_delta_w_list(current_w, not_update_w0, element[activ], nyt)
            not_update_w0 = copy.copy(tmp2)
            current_w = copy.copy(tmp)
            self.a_r_matrix = copy.copy(tmp)
            uvh_array[activ] = self.u_input_r(element[activ])

            ssuumm = numpy.sum(self.a_r_matrix)
            ssuumm += uvh_array[activ]

            #uvh_array = [self.u_input_r(element[i]) for i in range(len(element))]
            s = 'Сумма UвхR = ' + str(numpy.sum(current_w)) + '\n'
            print(s)
            print(ssuumm)
            l += 1

    def calculate_delta_w_list(self, current_w, not_update_w, index_array, nya):
        eps = 1e-7
        active = []
        passive = []
        for i in range(len(index_array)):
            if i not in not_update_w:
                if index_array[i] == 1:
                    active.append(i)
                else:
                    passive.append(i)

        func = self.delta_w #if len(not_update_w) == 0 else self.delta_w_with_flag
        dws = []

        ws = copy.copy(current_w)
        for i in range(len(current_w)):
            dw = 0.0
            if i not in not_update_w:
                dw = func(nya, len(active), len(index_array), False) if i in passive else func(nya, len(active), len(index_array), True)
                dw, fl = self.help_calc_delta_w(ws[i], dw)
                if fl:
                    if i not in not_update_w:
                        not_update_w.append(i)
                    #func = self.delta_w_with_flag
            dws.append(round(dw, 2))

        for i in range(len(current_w)):
            if i in active:
                current_w[i] -= dws[i]
            if i in passive:
                current_w[i] += dws[i]

            current_w[i] = round(current_w[i], 2)

            if current_w[i] <= 0.0:
                current_w[i] = 0.0
                if i not in not_update_w:
                    not_update_w.append(i)
            if current_w[i] >= 1.0:
                current_w[i] = 1.0
                if i not in not_update_w:
                    not_update_w.append(i)

        #current_w = [round(c, 2) for c in current_w]
        print(numpy.sum(current_w))

        return current_w, not_update_w




