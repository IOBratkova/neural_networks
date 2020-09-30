import copy
from classes.neuron import Neuron

class Calculating:
    def __init__(self):
        self.act_func = None
        self.letter_a1 = None
        self.letter_a2 = None
        self.letter_b1 = None
        self.letter_b2 = None
        self.letter_c = None
        self.neuron = None
        self.m = None

    # Обчающая выборка по буквам
    def make_m(self):
        if self.act_func[0] == 'Бинарная':
            self.m = self.__make_m_by_binary()
        elif self.act_func[0] == 'Биполярная':
            self.m = self.__make_m_by_bipolar()

    # Создание нейрона
    def create_neuron(self):
        count_input = len(self.letter_a1)
        count_input += 1
        count_output = 1
        function = self.act_func
        x_list = None
        # x_list = copy.copy(self.letter_a1)
        # x_list.insert(0, 1)
        self.neuron = Neuron(count_input, count_output, x_list, function)

    # Обчающая выборка для бинарной функции
    def __make_m_by_binary(self):
        a1 = copy.copy(self.letter_a1)
        a2 = copy.copy(self.letter_a2)
        b1 = copy.copy(self.letter_b1)
        b2 = copy.copy(self.letter_b2)
        return [(a1, 1), (a2, 1), (b1, 0), (b2, 0)]

    # Обчающая выборка для биполярной функции
    def __make_m_by_bipolar(self):
        a1 = [0 if not el else 1 for el in self.letter_a1]
        a2 = [0 if not el else 1 for el in self.letter_a2]
        b1 = [0 if not el else 1 for el in self.letter_b1]
        b2 = [0 if not el else 1 for el in self.letter_b2]
        return [(a1, 1), (a2, 1), (b1, -1), (b2, -1)]

    def calculate(self):
        self.create_neuron()
        print('>> нейрон')


