import copy
from classes.utils import *
from classes.neuron import Neuron
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

        # Обучающие выборки
        self.m_binary_list = None
        self.m_bipolar_list = None

        # Нейроны
        self.binary_neuron = None
        self.bipolar_neuron = None

        # Листы C1-C3 в разных вариантах
        self.c_list_binary = None
        self.c_list_bipolar = None

    # Создаёт две выборки
    def __make_ms(self):
        self.m_binary_list = self.__make_m_by_binary()
        self.m_bipolar_list = self.__make_m_by_bipolar()

    # Обчающая выборка для бинарной функции
    def __make_m_by_binary(self):
        a1 = copy.copy(self.letter_a1)
        a2 = copy.copy(self.letter_a2)
        b1 = copy.copy(self.letter_b1)
        b2 = copy.copy(self.letter_b2)
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, 0, 'B1 буква'), (b2, 0, 'B2 буква')]

    # Обчающая выборка для биполярной функции
    def __make_m_by_bipolar(self):
        a1 = make_bipolar_list(self.letter_a1)
        a2 = make_bipolar_list(self.letter_a1)
        b1 = make_bipolar_list(self.letter_a1)
        b2 = make_bipolar_list(self.letter_a1)
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, -1, 'B1 буква'), (b2, -1, 'B2 буква')]

    # Два листа Цешек - бинарны и биполярные
    def __make_c_lists(self):
        self.c_list_binary = self.__make_c_lists_binary()
        self.c_list_bipolar = self.__make_c_lists_bipolar()

    def __make_c_lists_bipolar(self):
        c1 = make_bipolar_list(self.letter_c1).insert(0, 1)  # make_bipolar_list(self.letter_c1)
        c2 = make_bipolar_list(self.letter_c2).insert(0, 1)  # make_bipolar_list(self.letter_c2)
        c3 = make_bipolar_list(self.letter_c3).insert(0, 1)  # make_bipolar_list(self.letter_c3)
        return [c1, c2, c3]

    def __make_c_lists_binary(self):
        c1 = copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c1)
        c2 = copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c2)
        c3 = copy_and_insert_one(self.letter_c1)  # copy.copy(self.letter_c3)
        return [c1, c2, c3]

    def teaching(self):
        print('\n>> ОБУЧЕНИЕ...')
        self.__make_ms()  # Создаем 2 обучющие выборки
        print('\nСозданые обучающие выборки: ')
        print('Бинарная: ', end='')
        print(self.m_binary_list)
        print('Биполярная: ', end='')
        print(self.m_bipolar_list)
