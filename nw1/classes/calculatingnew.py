import copy
from classes.neuron import Neuron
from classes.functions import ActivationFunctionConst


# TODO: необходимо посчитать входные суммарные сигналы и проделать "алгоритм чашина" с фигней про букву С и буквы Q
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

        # Листы C1-C3 в разных вариантах
        self.c_list_binary = None
        self.c_list_bipolar = None

        # Коэффициенты
        self.w_binary_list = None
        self.w_bipolar_list = None

        # Коэффициент плавности
        self.k = None

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
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, 0, 'B1 буква'), (b2, 0, 'B2 буква')]

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
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, -1, 'B1 буква'), (b2, -1, 'B2 буква')]

    # Два листа Цешек - бинарны и биполярные
    def __make_c_lists(self):
        self.c_list_binary = self.__make_c_lists_binary()
        self.c_list_bipolar = self.__make_c_lists_bipolar()

    def __make_c_lists_bipolar(self):
        c1 = [-1 if not el else 1 for el in self.letter_c1]
        c1.insert(0, 1)
        c2 = [-1 if not el else 1 for el in self.letter_c2]
        c2.insert(0, 1)
        c3 = [-1 if not el else 1 for el in self.letter_c3]
        c3.insert(0, 1)
        return [c1, c2, c3]

    def __make_c_lists_binary(self):
        c1 = self.copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c1)
        c2 = self.copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c2)
        c3 = self.copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c3)
        return [c1, c2, c3]

    # Создаем нейроны
    def __make_neuron(self):
        functions = ActivationFunctionConst()
        self.binary_neuron = Neuron(functions.binary_function, self.input_count)
        self.bipolar_neuron = Neuron(functions.bipolar_function, self.input_count)

    # Считаем все весовые коэффициенты
    def __calculate_w(self, neuron, m_list):
        for i in range(len(m_list)):
            j = i + 1
            y = copy.copy(m_list[i][1])
            x_list = copy.copy(m_list[i][0])
            print('w[' + str(j) + ']: ', end='')
            neuron.correction_w_list(x_list, y, self.k)
        return neuron.w_list

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
