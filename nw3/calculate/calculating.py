from calculate.utils import *
from calculate.neuron import Neuron
from calculate.adaline import Adaline
from calculate.functions import ActivationFunctionConst
import statistics


class Calculator:
    def __init__(self):
        self.symbols = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']
        self.letters_list = None
        self.letter_a1 = None
        self.letter_a2 = None
        self.letter_b1 = None
        self.letter_b2 = None
        self.letter_c1 = None
        self.letter_c2 = None
        self.letter_d1 = None
        self.letter_d2 = None
        self.letter_e1 = None
        self.letter_e2 = None
        self.letter_rs = None
        self.act_func = None
        self.neurons = None
        self.alpha = None
        self.avgs = None
        self.rs_s = None
        self.rs = None
        self.ss = None
        self.m = None
        self.k = None
        self.ws = None

    def teaching(self):
        print('\n>> ОБУЧЕНИЕ')
        self.__make_letters_list()
        print('\n>> Создание обучающих выборок')
        self.__make_all_m()
        print('\n>> Функция для создания нейронов - ' + self.act_func[0])
        self.__make_neurons()
        print('\n>> Инициализировано ' + str(len(self.letters_list)) + ' нейронов')
        self.__work()
        print('\n>> Суммарные входные сигналы')
        self.__calculate_ss()
        print('\n>> Среднее арифметическое')
        self.__calculate_avgs()

    def recognition(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        print('\n>> Буква для распознавания')
        self.__make_rs()
        print('\n>> Подсчет схожести')
        self.__calculate_gemini()
        print('\n>> Суммарный входной сигнал на разных нейронах')
        self.__calculate_s_for_rs()
        print('\n>> Результат')
        return self.__image_class()

    def __image_class(self):
        result = []
        for i in range(len(self.neurons)):
            j = i + 1
            r = self.neurons[i].function[1](self.rs_s[i], self.avgs[i])
            tr = r
            print(str(j) + ': ' + str(tr))
            result.append(tr)
        return result

    def __calculate_s_for_rs(self):
        result = []
        for i in range(len(self.letters_list)):
            j = i + 1
            s = self.neurons[i].calculate_s(self.rs)
            print(str(j) + '. ' + str(s))
            result.append(s)
        self.rs_s = result

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def __calculate_gemini(self):
        maximum = 0
        index = 0
        for i in range(len(self.letters_list)):
            j = i + 1
            s = 'Буква №' + str(j) + ': '
            letter = copy_and_insert_one(self.letters_list[i][0])
            tmp1 = self.__help_gemini(self.rs, letter)
            s += str(tmp1) + ', '
            letter = copy_and_insert_one(self.letters_list[i][1])
            tmp2 = self.__help_gemini(self.rs, letter)
            s += str(tmp2)
            max_tmp = tmp1 + tmp2
            if max_tmp >= maximum:
                maximum = max_tmp
                index = i
            print(s)
        print('Предположительно rs похожа на букву №' + str(index+1))

    def __make_rs(self):
        y = self.act_func[3]
        if self.letter_rs is not None:
            if y == (1, 0):
                rs = copy_and_insert_one(self.letter_rs)
                self.rs = rs
            if y == (1, -1):
                rs = [-1 if not x else 1 for x in self.letter_rs]
                rs.insert(0, 1)
                self.rs = rs

    def __make_all_m(self):
        res = []
        lst = self.__upd_by_functions()
        for i in range(5):
            j = i + 1
            print('m-' + str(j))
            tmp = self.__make_m_by_function(i, lst)
            res.append(tmp)
        self.m = res

    def __make_m_by_function(self, index, lst):
        result = []
        y = self.act_func[3]
        for i in range(len(lst)):
            if i == index:
                tmp1 = lst[i][0], y[0]
                tmp2 = lst[i][1], y[0]
                result.append(tmp1)
                result.append(tmp2)
                print(tmp1)
                print(tmp2)
            else:
                tmp1 = lst[i][0], y[1]
                tmp2 = lst[i][1], y[1]
                result.append(tmp1)
                result.append(tmp2)
                print(tmp1)
                print(tmp2)
        return result

    def __upd_by_functions(self):
        y = self.act_func[3]
        if y == (1, 0):
            return self.__upd_binary()
        if y == (1, -1):
            return self.__upd_bipolar()

    def __upd_binary(self):
        result = []
        for el in self.letters_list:
            tmp1 = copy_and_insert_one(el[0])
            tmp2 = copy_and_insert_one(el[1])
            result.append((tmp1, tmp2))
        return result

    def __upd_bipolar(self):
        result = []
        for el in self.letters_list:
            tmp1 = [-1 if not x else 1 for x in el[0]]
            tmp1.insert(0, 1)
            tmp2 = [-1 if not x else 1 for x in el[1]]
            tmp2.insert(0, 1)
            result.append((tmp1, tmp2))
        return result

    def __make_letters_list(self):
        self.letters_list = [
            (self.letter_a1, self.letter_a2),
            (self.letter_b1, self.letter_b2),
            (self.letter_c1, self.letter_c2),
            (self.letter_d1, self.letter_d2),
            (self.letter_e1, self.letter_e2)]

    def __make_neurons(self):
        count_input = len(self.letter_a2) + 1
        res = []
        tmp = ActivationFunctionConst().bipolar_delta_function
        if self.act_func[0] != tmp[0]:
            for i in range(len(self.letters_list)):
                neuron = Neuron(self.act_func, count_input)
                res.append(neuron)
            self.neurons = res
        else:
            alpha = copy.copy(self.alpha)
            for i in range(len(self.letters_list)):
                neuron = Adaline(self.act_func, count_input, alpha)
                res.append(neuron)
            self.neurons = res

    def __work(self):
        tmp = ActivationFunctionConst().bipolar_delta_function
        if self.act_func[0] != tmp[0]:
            self.__work_with_simple_neuron()
        else:
            self.__work_with_adaline()

    def __work_with_simple_neuron(self):
        print('\n>> Подсчет весовых коэффициентов для нейронов')
        self.__calculate_ws()
        # print('\n>> Суммарные входные сигналы')
        # self.__calculate_ss()
        # print('\n>> Среднее арифметическое')
        # self.__calculate_avgs()

    def __calculate_avgs(self):
        res = []
        for i in range(len(self.ss)):
            j = i + 1
            tmp = statistics.mean(self.ss[i])
            res.append(tmp)
            print(str(j) + ': ', end='')
            print(tmp)
        self.avgs = res

    def __calculate_ss(self):
        res = []
        for i in range(len(self.letters_list)):
            j = i + 1
            print('\nНейрон ' + str(j))
            neuron = self.neurons[i]
            m_list = self.m[i]
            tmp = self.__calculate_s(m_list, neuron)
            res.append(tmp)
        self.ss = res

    def __calculate_s(self, m_list, neuron):
        s_list = []
        for i in range(len(m_list)):
            s = neuron.calculate_s(m_list[i][0])
            s_list.append(s)
            print(self.symbols[i] + ', s = ' + str(s))
        return s_list

    def __calculate_ws(self):
        res = []
        for i in range(len(self.letters_list)):
            j = i + 1
            print('\nНейрон ' + str(j) + ' и его весовые коэффициенты:')
            neuron = self.neurons[i]
            m_list = self.m[i]
            tmp = self.__calculate_w(neuron, m_list)
            res.append(tmp)
        self.ws = res

    def __calculate_w(self, neuron, m_list):
        for i in range(len(m_list)):
            j = i + 1
            y = copy.copy(m_list[i][1])
            x_list = copy.copy(m_list[i][0])
            print('w[' + str(j) + ']: ', end='')
            neuron.correction_w_list(x_list, y, self.k)
        return neuron.w_list

    #АДАЛИН НИЖЕ

    def __work_with_adaline(self):
        print('\n>> Подсчет весовых коэффициентов для нейронов')
        self.__calculate_ws_adaline()

    def __calculate_ws_adaline(self):
        j = 1
        res = []
        for i in range(len(self.neurons)):
            print('\nРабота с нейроном №' + str(j) + '.......')
            neuron = self.neurons[i]
            m = self.m[i]
            j += 1
            self.__help_adaline(neuron, m)
            res.append(copy.copy(neuron.w_list))
        self.ws = res

    def __help_adaline(self, neuron, m):
        flag = False
        j = 1
        while not flag:
            print('\nИтерация №' + str(j))
            neuron.w_list_old = copy.copy(neuron.w_list)
            for i in range(len(m)):
                x_list = m[i][0]
                y = m[i][1]
                neuron.correction_w_list_with_adaline(x_list, y)
            flag, s = neuron.check_stop_rule()
            j += 1
            print('\ns = ' + str(s) + '. s <= eps? ' + str(flag))

        # self.__help_adaline(self.neurons[0], self.m[0])
        # # отработаем для нейрона №0
        # print('\n>> Взяли 0 нейрон')
        # neuron = self.neurons[0]  # берем 0 нейрон
        # print('\n>> Взяли 0 обучающую выборку')
        # m = self.m[0]  # берем 0 обучающую выборку
        # print('\n>> Пащетали')
        # neuron.w_list_old = copy.copy(neuron.w_list) # запомнили старый лист
        # neuron.correction_w_list_with_adaline(m[0][0], m[0][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[1][0], m[1][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[2][0], m[2][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[3][0], m[3][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[4][0], m[4][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[5][0], m[5][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[6][0], m[6][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[7][0], m[7][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[8][0], m[8][1])  # x_list, u_out
        # neuron.correction_w_list_with_adaline(m[9][0], m[9][1])  # x_list, u_out
        # res = neuron.check_stop_rule()
        # print(res)
