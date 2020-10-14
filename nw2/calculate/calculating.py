import statistics
from calculate.utils import *
from calculate.neuron import Neuron
from calculate.functions import ActivationFunctionConst


class Calculator:
    def __init__(self):
        # БУКВЫ
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
        self.letters_list = None
        self.rs = None

        self.symbols = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2', 'E1', 'E2']

        # M, K, Neurins, Ws, Ss
        self.m = None
        self.k = None
        self.neurons = None
        self.ws = None
        self.ss = None
        self.avgs = None
        self.rs_s = None

    def teaching(self):
        print('\n>> ОБУЧЕНИЕ')
        self.__make_letters_list()
        print('\n>> Создание обучающих выборок')
        self.__make_all_m()
        print('\n>> Создание нейронов на основе бинарной фунцкии')
        self.__make_neurons()
        print('\n>> Подсчет весовых коэффициентов для нейронов')
        self.__calculate_ws()
        print('\n>> Суммарные входные сигналы')
        self.__calculate_ss()
        print('\n>> Среднее арифметическое')
        self.__calculate_avgs()

    def recognition(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        print('\n>> Буква для распознавания')
        self.__make_rs_list_binary()
        print('\n>> Подсчет схожести')
        self.__calculate_gemini()
        print('\n>> Суммарный входной сигнал на разных нейронах')
        self.__calculate_s_for_rs()
        print('\n>> Результат')
        return self.__image_class()

    # Подсчёт сходства и вывод предположения о том, к какому классу будет относиться буква
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

    # Определяет класс изображения, вовзращая массив result,
    # где единица находится на том месте, какому классу отноится изображение
    def __image_class(self):
        result = []
        for i in range(len(self.neurons)):
            j = i + 1
            r = self.neurons[i].function[1](self.rs_s[i], self.avgs[i])
            print(str(j) + ': ' + str(r))
            result.append(r)
        return result

    # Помощь в подсчёте схожести (t - кол-во одинаковых символов для буквы а и б)
    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    # Подсчёт среднего значения для функции активации
    def __calculate_avgs(self):
        res = []
        for i in range(len(self.ss)):
            j = i + 1
            tmp = statistics.mean(self.ss[i])
            res.append(tmp)
            print(str(j) + ': ', end='')
            print(tmp)
        self.avgs = res

    # Подсчёт суммарных входных сигналов на нейронах для каждой буквы
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

    # Подсчет суммарного входного сигнала символа RS на каждом из нейронов
    def __calculate_s_for_rs(self):
        result = []
        for i in range(len(self.letters_list)):
            j = i + 1
            s = self.neurons[i].calculate_s(self.rs)
            print(str(j) + '. ' + str(s))
            result.append(s)
        self.rs_s = result

    # Вычисляет весовые коэффициенты для всех нейронов
    def __calculate_ws(self):
        res = []
        for i in range(len(self.letters_list)):
            j = i+1
            print('\nНейрон ' + str(j) + ' и его весовые коэффициенты:')
            neuron = self.neurons[i]
            m_list = self.m[i]
            tmp = self.__calculate_w(neuron, m_list)
            res.append(tmp)
        self.ws = res

    # Вычисляет весовые коэффициенты для нейрона
    def __calculate_w(self, neuron, m_list):
        for i in range(len(m_list)):
            j = i + 1
            y = copy.copy(m_list[i][1])
            x_list = copy.copy(m_list[i][0])
            print('w[' + str(j) + ']: ', end='')
            neuron.correction_w_list(x_list, y, self.k)
        return neuron.w_list

    # Создает список нейронов с бинарной функцией активации
    def __make_neurons(self):
        function = ActivationFunctionConst()
        count_input = len(self.letter_a2) + 1
        res = []
        for i in range(5):
            j = i+1
            print('Нейрон ' + str(j) + ' готов к бою')
            neuron = Neuron(function.binary_function, count_input)
            res.append(neuron)
        self.neurons = res

    # Создает обучающие выборки для всех классов букв
    def __make_all_m(self):
        res = []
        for i in range(5):
            j = i+1
            print('m-' + str(j))
            tmp = self.__make_m(i)
            res.append(tmp)
        self.m = res

    # Создает обучающую выборку,
    # устанавливая y = 1 для пар букв на месте index,
    # иначе y = 0
    def __make_m(self, index):
        result = []
        lst = self.__upd_binary_list()
        for i in range(len(lst)):
            if i == index:
                tmp1 = lst[i][0], 1
                tmp2 = lst[i][1], 1
                result.append(tmp1)
                result.append(tmp2)
                print(tmp1)
                print(tmp2)
            else:
                tmp1 = lst[i][0], 0
                tmp2 = lst[i][1], 0
                result.append(tmp1)
                result.append(tmp2)
                print(tmp1)
                print(tmp2)
        return result

    # Добавляет сдвиг (x[0])
    def __upd_binary_list(self):
        result = []
        for el in self.letters_list:
            tmp1 = copy_and_insert_one(el[0])
            tmp2 = copy_and_insert_one(el[1])
            result.append((tmp1, tmp2))
        return result

    # Создает лист буквы предназначенной для распознавания в бинарном представлении
    def __make_rs_list_binary(self):
        if self.letter_rs is not None:
            rs = copy_and_insert_one(self.letter_rs)
            print(rs)
            self.rs = rs

    # Создает сисок из символов для обучения
    def __make_letters_list(self):
        self.letters_list = [
            (self.letter_a1, self.letter_a2),
            (self.letter_b1, self.letter_b2),
            (self.letter_c1, self.letter_c2),
            (self.letter_d1, self.letter_d2),
            (self.letter_e1, self.letter_e2)]
