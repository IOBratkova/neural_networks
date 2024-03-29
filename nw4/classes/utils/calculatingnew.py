import math
import copy
from classes.neurons.neuron import Neuron
from classes.functions import ActivationFunctionConst


class Calculating:
    def __init__(self):
        # Буквы
        self.letter_a1 = None
        self.letter_a2 = None
        self.letter_b1 = None
        self.letter_b2 = None
        self.letter_c1 = None
        self.letter_c2 = None
        self.letter_c3 = None

        # Кол-во входов
        self.input_count = None

        # Обучающие выборки
        self.m_binary_list = None
        self.m_bipolar_list = None

        # Нейроны
        self.binary_neuron = None
        self.bipolar_neuron = None
        self.sigmoid_neuron = None

        # Листы C1-C3 в разных вариантах
        self.c_list_binary = None
        self.c_list_bipolar = None

        # Коэффициенты
        self.w_binary_list = None  # Ира
        self.w_bipolar_list = None

        # Коэффициент плавности
        self.k = None

        # Листсуммарных входных сигналов
        self.s_binary_list = []
        self.s_bipolar_list = []
        self.s_c_binary_list = []

        # Кукушки
        self.q_binary = None
        self.q_bipolar = None

        # Делители
        self.divider_binary = None
        self.divider_bipolar = None

        # T
        self.t = None

        # Avg
        self.avg_binary = None
        self.avg_bipolar = None

    def teaching(self):
        print('\n>> ОБУЧЕНИЕ...')
        self.input_count = len(self.letter_a1) + 1
        self.__make_ms()

        print('\nСозданые обучающие выборки: ')
        print('Бинарная: ', end='')
        print(self.m_binary_list)
        print('Биполярная: ', end='')
        print(self.m_bipolar_list)

        print('\nСозданы два нейрона на основе биполярной и бинарной функций ')
        self.__make_neuron()
        print('\nОбучение бинарного нейрона: ')
        self.w_binary_list = self.__calculate_w(self.binary_neuron, self.m_binary_list)
        print('\nОбучение биполярного нейрона: ')
        self.w_bipolar_list = self.__calculate_w(self.bipolar_neuron, self.m_bipolar_list)

        print('\nСуммарные входные сигналы:')
        self.__calculate_ss()
        self.avg_binary = (self.s_binary_list[0][0] + self.s_binary_list[1][0] + self.s_binary_list[2][0] +
                           self.s_binary_list[3][0]) / 4
        self.w_binary_list[0] -= self.avg_binary
        print('\navg (бинарное) = ' + str(self.avg_binary))

        self.avg_bipolar = (self.s_bipolar_list[0][0] + self.s_bipolar_list[1][0] + self.s_bipolar_list[2][0] +
                            self.s_bipolar_list[3][0]) / 4
        self.w_bipolar_list[0] -= self.avg_bipolar
        print('\navg (биполярное) = ' + str(self.avg_bipolar))
        self.__calculate_ss()

        print('\nQ1 и Q2:')
        self.__calculate_qs()

        print('\n!Далее работа продолжается с бинарной функцией активации!')
        t1 = self.__calculate_t(0.1, self.q_binary[0])
        t2 = self.__calculate_t(0.9, self.q_binary[1])
        print('\nЗначение t1 = ' + str(t1))
        print('Значение t2 = ' + str(t2))
        self.t = t1

    def recognition(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        print('\n!Работа ведётся с сигмоидальной функцией!')

        self.c_list_binary = self.__make_c_lists_binary()
        if not self.c_list_binary:
            print('Не введено ни одной буквы С')
        print('\nБуква(ы) С в бинарном представлении: ')
        print(self.c_list_binary)

        print('\n>> Сходство: ', end='')
        self.__calculate_gemini(self.c_list_binary, self.m_binary_list)

        self.sigmoid_neuron = copy.deepcopy(self.binary_neuron)
        self.sigmoid_neuron.function = ActivationFunctionConst().sigmoid_function
        print('\n>> Выбрана функция варианта - ' + self.sigmoid_neuron.function[0])

        print('\n>> Входной(ые) суммарные сигналы С: ')
        self.s_c_binary_list = self.__calculate_c_s(self.sigmoid_neuron)

        print('\n>> Согласно функции активации, изображение(я) принадлежит(ат) классу(ам): ')
        result1 = self.__classify(self.__get_image_class(self.sigmoid_neuron))
        print(result1)

        print('\n>> Сравним с функцией - ' + self.binary_neuron.function[0])

        print('\n>> Входной(ые) суммарные сигналы С: ')
        self.s_c_binary_list = self.__calculate_c_s(self.binary_neuron)

        print('\n>> Согласно функции активации, изображение(я) принадлежит(ат) классу(ам): ')
        result2 = self.__classify(self.__get_image_class(self.binary_neuron))
        print(result2)

        return result2

    def __calculate_c_s(self, neuron):
        res = self.__calculate_s(self.c_list_binary, neuron)
        return res

    def __classify(self, list):
        result = []
        for r in list:
            tmp = self.binary_neuron.function[1](r[0], 0)
            result.append((tmp, r[1]))
        return result

    def __get_image_class(self, neuron):
        result = []
        for i in range(len(self.c_list_binary)):
            if neuron.function[0] == 'Бинарная':
                res = neuron.function[1](self.s_c_binary_list[i][0], self.avg_binary)
                result.append((round(res[0]), self.s_c_binary_list[i][1]))
                print(round(res[0]))
            else:
                res = neuron.function[1](self.s_c_binary_list[i][0], self.avg_binary)
                result.append((round(res), self.s_c_binary_list[i][1]))
                print(round((res)))
        return result

    def __calculate_gemini(self, list_c, list_letters):
        for row in list_c:
            print('\n' + row[1] + ': ')
            for letter in list_letters:
                tmp = self.__help_gemini(row[0], letter[0])
                print(letter[1] + ' =>> ' + str(tmp))

    # Подсчёт схожести
    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def copy_and_insert_one(self, list):
        result = copy.deepcopy(list)
        result.insert(0, 1)
        return result

    # Создаёт две выборки
    def __make_ms(self):
        self.m_binary_list = self.__make_m_by_binary()
        self.m_bipolar_list = self.__make_m_by_bipolar()

    # Обчающая выборка для бинарной функции
    def __make_m_by_binary(self):
        a1 = self.copy_and_insert_one(self.letter_a1)
        a2 = self.copy_and_insert_one(self.letter_a2)
        b1 = self.copy_and_insert_one(self.letter_b1)
        b2 = self.copy_and_insert_one(self.letter_b2)
        return [(a1, 'A1', 1), (a2, 'A2', 1), (b1, 'B1', 0), (b2, 'B2', 0)]

    # Обчающая выборка для биполярной функции
    def __make_m_by_bipolar(self):
        a1 = [-1 if not el else 1 for el in self.letter_a1]
        a1.insert(0, 1)
        a2 = [-1 if not el else 1 for el in self.letter_a2]
        a2.insert(0, 1)
        b1 = [-1 if not el else 1 for el in self.letter_b1]
        b1.insert(0, 1)
        b2 = [-1 if not el else 1 for el in self.letter_b2]
        b2.insert(0, 1)
        return [(a1, 'A1', 1), (a2, 'A2', 1), (b1, 'B1', -1), (b2, 'B2', -1)]

    # Два листа Цешек - бинарны и биполярные
    def __make_c_lists(self):
        self.c_list_binary = self.__make_c_lists_binary()
        self.c_list_bipolar = self.__make_c_lists_bipolar()

    # Создает "биполярный" список по букве С
    def __make_c_lists_bipolar(self):
        result_list = []
        if self.letter_c1 is not None:
            c1 = [-1 if not el else 1 for el in self.letter_c1]
            c1.insert(0, 1)
            result_list.append((c1, 'C1'))
        if self.letter_c2 is not None:
            c2 = [-1 if not el else 1 for el in self.letter_c2]
            c2.insert(0, 1)
            result_list.append((c2, 'C2'))
        if self.letter_c3 is not None:
            c3 = [-1 if not el else 1 for el in self.letter_c3]
            c3.insert(0, 1)
            result_list.append((c3, 'C3'))
        return result_list

    # Создает "бинарный" список по букве С
    def __make_c_lists_binary(self):
        result_list = []
        if self.letter_c1 is not None:
            c1 = self.copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c1)
            result_list.append((c1, 'C1'))
        if self.letter_c2 is not None:
            c2 = self.copy_and_insert_one(self.letter_c2)  # copy.copy(self.letter_c2)
            result_list.append((c2, 'C2'))
        if self.letter_c3 is not None:
            c3 = self.copy_and_insert_one(self.letter_c3)  # copy.copy(self.letter_c3)
            result_list.append((c3, 'C3'))
        return result_list

    # Создаем нейроны
    def __make_neuron(self):
        functions = ActivationFunctionConst()
        self.binary_neuron = Neuron(functions.binary_function, self.input_count)
        self.bipolar_neuron = Neuron(functions.bipolar_function, self.input_count)

    # Считаем все весовые коэффициенты
    def __calculate_w(self, neuron, m_list):
        for i in range(len(m_list)):
            j = i + 1
            y = copy.copy(m_list[i][2])
            x_list = copy.copy(m_list[i][0])
            print('w[' + str(j) + ']: ', end='')
            neuron.correction_w_list(x_list, y, self.k)
        return neuron.w_list

    def __calculate_ss(self):
        print('Бинарные: ')
        self.s_binary_list = self.__calculate_s(self.m_binary_list, self.binary_neuron)
        print('Биполярные: ')
        self.s_bipolar_list = self.__calculate_s(self.m_bipolar_list, self.bipolar_neuron)

    # Считаем входные суммарные сигналы
    def __calculate_s(self, m_list, neuron):
        s_list = []
        for i in range(len(m_list)):
            s = neuron.calculate_s(m_list[i][0])
            s_list.append((s, m_list[i][1]))
            print(m_list[i][1] + ', s = ' + str(s))
        return s_list

    def __calculate_qs(self):
        self.q_binary, self.divider_binary = self.__calculate_q1_q1(self.s_binary_list)
        print('Бинарные: ', end='')
        print('s2(cp) = ' + str(self.divider_binary[1]), end='')
        print(' | q1 = ' + str(self.q_binary[0]), end='')
        print(' | q2 = ' + str(self.q_binary[1]), end='')
        print(' | s1(cp) = ' + str(self.divider_binary[0]), end='')
        self.q_bipolar, self.divider_bipolar = self.__calculate_q1_q1(self.s_bipolar_list)
        print('\nБиполярные: ', end='')
        print('s2(cp) = ' + str(self.divider_bipolar[1]), end='')
        print(' | q1 = ' + str(self.q_bipolar[0]), end='')
        print(' | q2 = ' + str(self.q_bipolar[1]), end='')
        print(' | s1(cp) = ' + str(self.divider_bipolar[0]), end='')

    def __calculate_q1_q1(self, s_list):
        divider_a = (s_list[0][0] + s_list[1][0]) / 2  # s1ср
        divider_b = (s_list[2][0] + s_list[3][0]) / 2  # s1ср
        result = divider_a - divider_b
        q = result / 3
        center = (divider_b + divider_a) / 2
        tmp = q / 2
        q1 = center - tmp
        q2 = center + tmp
        return (q1, q2), (divider_a, divider_b)

    def __calculate_t(self, y, q):
        ln = -math.log((1 / y) - 1)
        return ln / q
