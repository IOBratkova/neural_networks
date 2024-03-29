import random
import numpy
import copy


class Perceptron:
    def __init__(self, count_s, count_a, count_r, w_range=(0.0, 0.1)):
        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.count_s = count_s
        self.count_a = count_a
        self.count_r = count_r
        self.a_r_matrix = numpy.random.sample((self.count_r, self.count_a)) * (w_range[1] - w_range[0]) + w_range[0]
        self.s_a_matrix = numpy.random.sample((self.count_a, self.count_s)) * (w_range[1] - w_range[0]) + w_range[0]

        #self.s_a_matrix = self.get_w(w_range, self.count_s, self.count_a)#[[random.uniform(w_range[0], w_range[1]) for _ in range(self.count_s)]
                           #for _ in range(self.count_a)]
        # self.a_r_matrix = self.get_w(w_range, self.count_a, self.count_r)
            #[[random.uniform(w_range[0], w_range[1]) for _ in range(self.count_a)]
             #              for _ in range(self.count_r)]
        #[random.uniform(w_range[0], w_range[1]) for _ in range(len(self.count_a))]

    def get_w(self, w_range, count1, count2):
        result = []
        for i in range(count1):
            t = [random.uniform(w_range[0], w_range[1]) for _ in range(count2)]
            result.append(t)
        return result

    def u_input_all_a(self, lst):
        c = 1.0 * numpy.sum(lst)
        res = []
        for i in range(self.count_a):
            ts = []
            for j in range(self.count_s):
                t = lst[j] * self.s_a_matrix[i][j]
                ts.append(t)
            r = numpy.sum(ts)
            res.append(r)
        return numpy.array(res) / c

    def u_input_r(self, lst, index):
        r = [lst[j] * self.a_r_matrix[index][j] for j in range(self.count_a)]
        return numpy.sum(r)

    def get_excitatory_neurons(self, letter):
        array = [i for i in range(len(letter)) if letter[i] == 1]
        return array

    def delta_w(self, ny, nak, n, flag):
        return (ny - (nak * ny / n)) if flag else -(nak*ny/n)


    def gamma_correction(self, uvh_array, nyt, element, teta):
        teta_new = copy.copy(teta)

        megaiter = 0
        for i in range(len(element)):
            tmp_elem = []
            for j in range(len(element)):
                if i != j:
                    tmp_elem.append([0 if v == 1 else 1 for v in element[j]])
                else:
                    tmp_elem.append(element[i])
            l = 0
            lastSignal = uvh_array[i][i]
            while True:
                k = megaiter + 1
                print('t' + str(k).translate(self.SUB) + ':\n')
                activ = self._select_element(teta_new[i], uvh_array[i], l, i)
                if activ is None:
                    print('канец')
                    break
                self.calc_Ilia(tmp_elem[activ], self.a_r_matrix[i], nyt)

                for z in range(len(uvh_array[i])):
                    uvh_array[i][z] = self.u_input_r(element[z], i)

                # if lastSignal < uvh_array[i][i]:
                #     self.calc_Ilia(tmp_elem[i], self.a_r_matrix[i], nyt)
                #     for z in range(len(uvh_array[i])):
                #         uvh_array[i][z] = self.u_input_r(element[z], i)
                # lastSignal = uvh_array[i][i]

                # if not self.__requiredContinue(teta_new[i], uvh_array[i], i):
                #     print('канец')
                #     break
                #
                # bestIndex = -1
                # bestValue = -1
                # matrix = copy.copy(self.a_r_matrix[i])
                # for image in range(len(tmp_elem)):
                #     self.calc_Ilia(tmp_elem[image], self.a_r_matrix[i], nyt)
                #     value = 0
                #     for z in range(len(uvh_array[i])):
                #         if z == i:
                #             value += self.u_input_r(element[z], i) - uvh_array[i][z]
                #         else:
                #             value += uvh_array[i][z] - self.u_input_r(element[z], i)
                #     if value > bestValue:
                #         bestValue = value
                #         bestIndex = image
                #     self.a_r_matrix[i] = copy.copy(matrix)
                #
                # if bestValue < 1e-7:
                #     bestIndex = self._select_element(teta_new[i], uvh_array[i], l, i)
                #
                # self.calc_Ilia(tmp_elem[bestIndex], self.a_r_matrix[i], nyt)
                # for z in range(len(uvh_array[i])):
                #     uvh_array[i][z] = self.u_input_r(element[z], i)

                s = 'Сумма UвхR = ' + str(numpy.sum(self.a_r_matrix)) + '\n'
                print(s)
                l += 1
                megaiter += 1

    def _select_element(self, teta, uvh, l, imagen):
        list_inv = []
        if uvh[imagen] < teta:
            list_inv.append(imagen)
        for i in range(len(uvh)):
            if i == imagen:
                continue
            if uvh[i] >= teta:
                list_inv.append(i)
        if len(list_inv) == 0:
            return None
        return list_inv[l % len(list_inv)]

    def __requiredContinue(self, teta, uvh, imagen):
        list_inv = []
        if uvh[imagen] < teta:
            list_inv.append(imagen)
        for i in range(len(uvh)):
            if i == imagen:
                continue
            if uvh[i] >= teta:
                list_inv.append(i)
        if len(list_inv) == 0:
            return False
        return True




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
            if abs(w + 1) < eps and i in passive:
                passive.remove(i)
                continue
            max_dw = 1 - w if i in active else w + 1
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
