import random
import sys

from classes.utils.utils import *
from new_per.perceptron_new import Perceptron
import numpy
import copy


class Calculating:
    def __init__(self):
        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.ny = 0.2
        self.letter_a1 = None
        self.letter_b1 = None
        self.letter_a2 = None
        self.letter_b2 = None
        self.letter_c1 = None
        self.letter_c2 = None
        self.letter_r1 = None
        self.letter_r2 = None
        self.letter_r3 = None
        self.m_array = None
        self.letters_list = None  #
        self.perceptron = None

        self.m_c = None
        self.excitatory_neurons = None
        self.a_inputs_signals = None  # UAвх
        self.threshold_array = None
        self.threshold_one = None
        self.threshold_all = None
        self.r_input_signals = None  # URвх
        self.r_input_signals_info = None
        self.r_input_signals_teta = None  # URвх
        self.flags = None
        self.c_s = None
        self.ex_as = None
        self.a_gem = None
        self.b_gem = None
        self.all_signals = None
        self.all_r_signals = None
        self.teta_r = None

    def teaching(self, w_range, count_a):
        print('\n>> ОБУЧЕНИЕ...')
        count_s = len(self.letter_a1)
        self.letters_list = self.__make_letters_list()
        if len(self.letters_list) == 0:
            return None
        count_r = len(self.letters_list)
        self.m_array = self.__make_all_m()
        print('\nА-элементов = ' + str(count_a))
        print('S-элементов = ' + str(count_s))
        print('Диапазон весов = ' + str(w_range) + '\n')

        result = None
        okey = False
        while not okey:
            okey = True
            self.perceptron = Perceptron(count_s, count_a, count_r, w_range)
            #self.omegamind_init()
            self.excitatory_neurons = self.__get_excitatory_neurons()
            self.a_inputs_signals = self.__get_a_elements_input_signals()
            self.all_signals = self.__get_threshold_value_for_neurons()
            if len(self.all_signals) == 0:
                okey = False
                continue

            result = self.__calculate_r()
            if result is None:
                okey = False
                continue
        self.all_r_signals = result[0]
        self.teta_r = result[1]
        uvh_array = self.perceptron.gamma_correction(self.all_r_signals, 0.1, self.all_signals, self.teta_r)

    def omegamind_init(self):
        array = numpy.average(numpy.array(self.letters_list).transpose(), axis=1)
        perceptron = self.perceptron
        for row in perceptron.s_a_matrix:
            for i in range(len(row)):
                row[i] = array[i] + random.uniform(-0.3, 0.3)
                row[i] = 0 if row[i] < 0 else row[i]
                row[i] = 1 if row[i] > 1 else row[i]
        pass

    def __sub_signals(self, a, b):
        #1 - 1 = 0, 0 - 1 = 0, 1 - 0 = 1, 0 - 0 = 0
        return [1 if a[i] == 1 and b[i] == 0 else 0 for i in range(len(a))]

    def __calculate_r(self):
        a = self.all_signals[0]
        b = self.all_signals[1]
        c = self.all_signals[2]

        ab = numpy.sum(self.__sub_signals(a, b))
        ac = numpy.sum(self.__sub_signals(a, c))
        a_av = numpy.average([ab, ac])

        ba = numpy.sum(self.__sub_signals(b, a))
        bc = numpy.sum(self.__sub_signals(b, c))
        b_av = numpy.average([ba, bc])

        ca = numpy.sum(self.__sub_signals(c, a))
        cb = numpy.sum(self.__sub_signals(c, b))
        c_av = numpy.average([ca, cb])

        #===============a======================
        min_a = numpy.min([ab, ac])
        min_not_a = numpy.min([ba, bc, ca, cb])
        if min_a == min_not_a and min_a == 0:
            return None
        # avg_a = numpy.average([min_a, -min_not_a])
        avg_a = numpy.average([a_av, -numpy.average([b_av, c_av])])
        if avg_a > min_a:
            avg_a = min_a - 1e-7
        if avg_a < -min_not_a:
            avg_a = -min_not_a + 1e-7

        # ==============b======================
        min_b = numpy.min([ba, bc])
        min_not_b = numpy.min([ab, ac, ca, cb])
        if min_b == min_not_b and min_b == 0:
            return None

        # avg_b = numpy.average([min_b, -min_not_b])
        avg_b = numpy.average([b_av, -numpy.average([a_av, c_av])])
        if avg_b > min_b:
            avg_a = min_b - 1e-7
        if avg_b < -min_not_b:
            avg_b= -min_not_b + 1e-7

        # ==============c======================
        min_c = numpy.min([ca, cb])
        min_not_c = numpy.min([ab, ac, ba, cb])
        if min_c == min_not_c and min_c == 0:
            return None
        # avg_c = numpy.average([min_c, -min_not_c])
        avg_c = numpy.average([c_av, -numpy.average([a_av, b_av])])
        if avg_c > min_c:
            avg_c = min_c - 1e-7
        if avg_c < -min_not_c:
            avg_c = -min_not_c + 1e-7

        list_active = []
        per = self.perceptron
        list_active.append([per.u_input_r(a, 0), per.u_input_r(a, 1), per.u_input_r(a, 2)])
        list_active.append([per.u_input_r(b, 0), per.u_input_r(b, 1), per.u_input_r(b, 2)])
        list_active.append([per.u_input_r(c, 0), per.u_input_r(c, 1), per.u_input_r(c, 2)])

        return list_active, [avg_a, avg_b, avg_c]
        # res = []
        # for i in range(len(self.perceptron.a_r_matrix)):
        #     t0 = self.perceptron.u_input_r(self.all_signals[0], i)
        #     t1 = self.perceptron.u_input_r(self.all_signals[1], i)
        #     t2 = self.perceptron.u_input_r(self.all_signals[2], i)
        #     res.append([t0, t1, t2])
        # print('эрочки (от слова "эротика"): \n')
        # print(res)
        # teta0 = numpy.average(res[0])
        # teta1 = numpy.average(res[1])
        # teta2 = numpy.average(res[2])
        # res = []
        # for i in range(len(self.perceptron.a_r_matrix)):
        #     res.append(self.perceptron.u_input_r(self.all_signals[i], i))
        # return res, [teta0, teta1, teta2]

    def __make_letters_list(self):
        res = []
        if self.letter_a1 is not None: #and self.letter_a2 is not None:
            res.append(self.letter_a1) #, self.letter_a2)
        if self.letter_b1 is not None:# and self.letter_b2 is not None:
            res.append(self.letter_b1) #, self.letter_b2)
        if self.letter_c1 is not None:# and self.letter_c2 is not None:
            res.append(self.letter_c1) #, self.letter_c2)
        return res

    def __get_a_elements_input_signals(self):
        res = []
        s = '\nСигналы на входах А-элементов: \n'
        for i in range(len(self.letters_list)):
            j = i + 1
            s += 'i' + str(j).translate(self.SUB) + ': \n'
            r1 = self.perceptron.u_input_all_a(self.letters_list[i])
            # r2 = self.perceptron.u_input_all_a(self.letters_list[i][1])
            res.append(r1)
            s += str(r1) + '\n'
            # s += str(r2) + '\n'
        print(s)
        return res

    def __get_excitatory_neurons(self):
        s = '\nВозбуждаемые нейроны, нумерация ведётся с 0: \n'
        res = []
        for i in range(len(self.letters_list)):
            j = i + 1
            s += 'i' + str(j).translate(self.SUB) + ': \n'
            r1 = self.perceptron.get_excitatory_neurons(self.letters_list[i])
            # r2 = self.perceptron.get_excitatory_neurons(self.letters_list[i][1])
            res.append(r1)
            s += str(r1) + '\n'
            # s += str(r2) + '\n'
        print(s)
        return res

    def __make_all_m(self):
        res = []
        for i in range(len(self.letters_list)):
            j = i + 1
            print('m-' + str(j))
            tmp = self.__make_m(i)
            res.append(tmp)
        return res

    def __upd_binary_list(self):
        result = []
        for el in self.letters_list:
            tmp1 = copy_and_insert_one(el)
            #tmp2 = copy_and_insert_one(el[1])
            result.append(tmp1)
        return result

    def __make_m(self, index):
        result = []
        lst = self.__upd_binary_list()
        for i in range(len(lst)):
            if i == index:
                tmp1 = lst[i], 1
                # tmp2 = lst[i], 1
                result.append(tmp1)
                # result.append(tmp2)
                print(tmp1)
                # print(tmp2)
            else:
                tmp1 = lst[i], -1
                # tmp2 = lst[i], -1
                result.append(tmp1)
                # result.append(tmp2)
                print(tmp1)
                # print(tmp2)
        return result

    def __get_answer_by_teta_a__(self, list):
        print(list)
        for i in range(len(list)):
            signal_1 = list[i]
            count = numpy.sum(signal_1)
            count /= float(len(signal_1))
            # if count < 0.1:
            #     print('Все пропало, Шеф 1\n')
            #     exit(-1)
            #     return False
            for j in range(i + 1, len(list)):
                signal_2 = list[j]
                div_signal = [1.0 if signal_1[k] != signal_2[k] else 0.0 for k in range(len(signal_1))]
                count = numpy.sum(div_signal)
                if count / len(div_signal) < 0.5:
                    print('Все пропало, Шеф 2\n')
                    return False
        print('Выпьем\n')
        return True

    def __get_threshold_value_for_neurons(self):
        s = '\nПороговые значения для каждого А-элмента: \n'
        a11 = []
        for i in range(len(self.a_inputs_signals[0])):
            a11.append((self.a_inputs_signals[0][i] + self.a_inputs_signals[1][i] + self.a_inputs_signals[2][i]) / 3)

        # min_arr = []
        # max_arr = []
        # for i in range(len(self.a_inputs_signals[0])):
        #     min_arr.append(
        #         numpy.min([self.a_inputs_signals[0][i], self.a_inputs_signals[1][i], self.a_inputs_signals[2][i]]))
        #     max_arr.append(
        #         numpy.max([self.a_inputs_signals[0][i], self.a_inputs_signals[1][i], self.a_inputs_signals[2][i]]))
        #
        # for i in range(len(min_arr)):
        #     a11.append(random.uniform(min_arr[i], max_arr[i]))

        print('\n===============================')
        # print(a11)
        # print(b11)
        # print(c11)
        print('===============================')

        self.a_treshold_one = a11
        all_signals = []
        for input_signal in self.a_inputs_signals:
            output_signal = [1 if input_signal[i] >= self.a_treshold_one[i] else 0 for i in
                             range(len(self.a_treshold_one))]
            all_signals.append(output_signal)
        return all_signals if self.__get_answer_by_teta_a__(all_signals) else []

    # def get_r_elements_input_signals(self):
    #     self.r_input_signals_teta = []
    #     self.r_input_signals_info = []
    #     self.r_input_signals = []
    #     flags = []
    #     for element in self.threshold_array:
    #         print(element[1] + ': ')
    #         res, teta, info = self.check_r(element)
    #         flag = True if info[0] == self.m_array[0][1] and info[1] == self.m_array[1][1] else False
    #         print('настройка перцептрона не требуется\n') if flag else print('требуется настройка перцептрона!!\n')
    #         flags.append(flag)
    #         self.r_input_signals_teta.append(teta)
    #         self.r_input_signals_info.append(info)
    #         self.r_input_signals.append(res)
    #     self.flags = flags
    #
    # def check_r(self, element):
    #     res = [self.perceptron.u_input_r(el) for el in element[0]]
    #     # self.r_input_signals.append(res)
    #     s = 'Вектор UвхR = ' + str(res)
    #     teta = (res[0] + res[1]) / 2
    #     s += '. Пороговое значение, Rθ = ' + str(teta) + '.\n'
    #     s += 'Таким образом: ' + str(res[0])
    #     s += ' >= ' + str(teta)
    #     s += ' > ' + str(res[1]) + '. '
    #     info = [1 if res[i] >= teta else -1 for i in range(len(res))]
    #     s += '\nПри подаче исходных сообщений имеем: ' + str(info)
    #     s += '. Изначально имеем: ' + str([self.m_array[0][1], self.m_array[1][1]]) + ' => '
    #     print(s, end='')
    #     return (res, teta, info)

        #print('\nИндивидуальные пороги для А-элементов: ')
        # a = self.a_inputs_signals[0]
        # b = self.a_inputs_signals[1]
        # res1 = [1 if a[i] >= self.threshold_one[i] else 0 for i in range(len(self.threshold_one))]
        # res2 = [1 if b[i] >= self.threshold_one[i] else 0 for i in range(len(self.threshold_one))]
        # print(str(self.letters_array[0][1]) + ': ' + str(res1))
        # print(str(self.letters_array[1][1]) + ': ' + str(res2))
        # return [res1, res2] if self.answer_about_teta(res1, res2, 'Индивидуальные пороги для всех нейронов') else None

# 0.1 0.3 0.4
# 0.1 0.3 0.4
# [0.6394320756745233, 0.7361021091812208, 0.7766753672584352, 0.5985731868891857, 0.6657128141097408, 0.7673141821711915, 0.7682479705745008, 0.7497159631228463, 0.5955681373185483, 0.7325878022368126, 0.5442842143926607, 0.5787323990001365]


# a = self.a_inputs_signals[0]
# b = self.a_inputs_signals[1]
# res = [(a[i] + b[i]) / 2 for i in range(len(a))]
# [print('Пороговое значение для A' + str(i).translate(self.SUB) + ', θ = ' + str(res[i])) for i in
#  range(len(res))]
# return res

#     def teaching(self, w_range, count_a):
# #        self.perceptron.print_info()
#
#
#         self.threshold_info()
#         self.check_threshold()
#         self.get_r_elements_input_signals()
#         self.r_input_signals_teta[0] = self.gamma_correct()
#         a = self.perceptron.u_input_all_a(self.letter_a1[0])
#         b = self.perceptron.u_input_all_a(self.letter_b1[0])
#         tetas = [((a[i] + b[i]) / 2) for i in range(len(a))] #self.threshold_one
#         res1 = [1 if a[i] >= tetas[i] else 0 for i in range(len(tetas))]
#         res2 = [1 if b[i] >= tetas[i] else 0 for i in range(len(tetas))]
#         resRa = self.perceptron.u_input_r(res1)
#         resRb = self.perceptron.u_input_r(res2)
#         teta = (resRa + resRb) / 2
#         self.r_input_signals_teta[0] = teta #
#         # print(teta)
#         # print(self.r_input_signals_teta[0])
#         # print(str(numpy.average([teta, self.r_input_signals_teta[0]])))
#         #self.r_input_signals_teta[0] = (teta+self.r_input_signals_teta[0])/2
#         print('============!!!=============')


    def recognition(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        self.m_c = None
        self.c_s = None
        self.ex_as = None
        self.c_r = None
        y = None
        self.m_c = copy_and_insert_one(self.letter_r1)
        print('\n>> Схожесть буквы С с каждой из буков: ')
        self.__calculate_gemini()
        print('\n>> Входной суммарный сигнал С (A-S), реакция на пороги: ')
        self.c_s, self.ex_as = self.__calculate_w_as()
        print('\n>> Входной суммарный сигнал С (A-R): ')
        self.c_r, y = self.__calculate_w_rs()

        return y

    def __calculate_w_as(self):
        s = self.perceptron.u_input_all_a(self.letter_r1)
        tetas = self.a_treshold_one
        res1 = [1 if s[i] >= tetas[i] else 0 for i in range(len(tetas))]
        print('teta = ' + str(tetas))
        print('сигнал = ' + str(s))
        print('результат = ' + str(res1))
        return s, res1

    def __calculate_w_rs(self):
        ex_as = self.ex_as
        res0 = self.perceptron.u_input_r(ex_as, 0)
        res1 = self.perceptron.u_input_r(ex_as, 1)
        res2 = self.perceptron.u_input_r(ex_as, 2)
        print(res0)
        print(res1)
        print(res2)
        teta = self.teta_r
        print(teta)

        y0 = 1 if res0 >= teta[0] else -1
        y1 = 1 if res1 >= teta[1] else -1
        y2 = 1 if res2 >= teta[2] else -1

        best_index = -1
        max_value = -sys.float_info.max
        k = [(res0 - teta[0]), (res1 - teta[1]), (res2 - teta[2])]
        for i in range(len(k)):
            if max_value < k[i]:
                best_index = i
                max_value = k[i]


        print('первый раз осознал недостатки, они такие:')
        print(best_index)

        print('осознал свои недостатки, поделюсь с желающими бесценным опытом:')
        print(y0)
        print(y1)
        print(y2)

        return [], y1
#
    def __calculate_gemini(self):
        self.a_gem = self.__help_gemini(self.letter_r1, self.letter_a1)
        print('А1 + R: ' + str(self.a_gem))
        self.b_gem = self.__help_gemini(self.letter_r1, self.letter_b1)
        print('B1 + R: ' + str(self.b_gem))
        self.c_gem = self.__help_gemini(self.letter_r1, self.letter_c1)
        print('C1 + R: ' + str(self.c_gem))

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

