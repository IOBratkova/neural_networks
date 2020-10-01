import copy
from classes.neuron import Neuron
from classes.functions import ActivationFunctionConst


class Calculating:
    def __init__(self):
        self.act_func = ActivationFunctionConst().bipolar_function  # По умолчанию биполярная функция
        self.letter_a1 = None  # Символ А1, исходный todo: положить сюда данные для выборки
        self.letter_a2 = None  # Символ А2, исходный
        self.letter_b1 = None  # Символ В1, исходный
        self.letter_b2 = None  # Символ В2, исходный
        self.letter_c = None  # Символ C для распознавания
        self.neuron = None  # Нейрон
        self.m_list = []    # Обучающая выборка
        self.s_list = []    # Вектор входных обучающих сигналов по буквам
        self.c = []         # Буква С
        self.divider = None # Порог для функций
        self.k = 1.0 # Коэффициент к для "плавности"

    # Обчающая выборка по буквам
    def make_m(self):
        if self.act_func[0] == 'Бинарная':
            self.m_list = self.__make_m_by_binary()
        elif self.act_func[0] == 'Биполярная':
            self.m_list = self.__make_m_by_bipolar()
        else:
            self.m_list = self.__make_m_by_bipolar()

    # Символ с для распознавания
    def make_c(self):
        if self.act_func[0] == 'Бинарная':
            self.c = copy.copy(self.letter_c)
            self.c.insert(0, 1)
        elif self.act_func[0] == 'Биполярная':
            self.c = [-1 if not el else 1 for el in self.letter_c]
            self.c.insert(0, 1)
        else:
            self.c = [-1 if not el else 1 for el in self.letter_c]
            self.c.insert(0, 1)

    # Создание нейрона
    def create_neuron(self, list):
        count_input = len(list) + 1
        count_output = 1
        function = self.act_func
        self.neuron = Neuron(count_input, count_output, function)

    # Обчающая выборка для бинарной функции
    def __make_m_by_binary(self):
        a1 = copy.copy(self.letter_a1)
        a2 = copy.copy(self.letter_a2)
        b1 = copy.copy(self.letter_b1)
        b2 = copy.copy(self.letter_b2)
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, 0, 'B1 буква'), (b2, 0, 'B2 буква')]

    # Обчающая выборка для биполярной функции
    def __make_m_by_bipolar(self):
        a1 = [-1 if not el else 1 for el in self.letter_a1]
        a2 = [-1 if not el else 1 for el in self.letter_a2]
        b1 = [-1 if not el else 1 for el in self.letter_b1]
        b2 = [-1 if not el else 1 for el in self.letter_b2]
        return [(a1, 1, 'A1 буква'), (a2, 1, 'A2 буква'), (b1, -1, 'B1 буква'), (b2, -1, 'B2 буква')]

    # Обучить нейрон
    def teaching(self):
        print('\n>> ОБУЧЕНИЕ...')
        self.make_m()  # Создали обучающую выборку
        print('\n>> Создано обучающее множество М ')
        self.create_neuron(self.m_list[0][0])  # Создали нейрон
        print('\n>> Создан нейрон')
        print('\n>> Подсчёт весовых коэффициентов: ')
        self.__calculate_w()
        print('\n>> Входные суммарные сигналы: ')
        self.__calculate_s()
        print('\n>> Подходящий порог: ')
        self.__avg_divider()
        print('divider = ' + str(self.divider))

    def recognize(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        self.make_c()
        print('\n>> Схожесть буквы С с каждой из буков: ')
        self.__calculate_gemini()
        print('\n>> Входной суммарный сигнал С: ')
        s = self.neuron.calculate_s(self.c)
        print('s = ' + str(s))
        print('\n>> Согласно функции активации, изображение принадлежит классу: ')
        result = self.act_func[1](s, self.divider)
        print(result[1])
        return result

    # Считаем все весовые коэффициенты
    def __calculate_w(self):
        for i in range(len(self.m_list)):
            x_list = copy.copy(self.m_list[i][0])
            x_list.insert(0, 1)
            y = copy.copy(self.m_list[i][1])
            j = i + 1
            print('w[' + str(j) + ']: ', end='')
            self.neuron.correction_w_list(x_list, y, self.k)

    # Считаем входные суммарные сигналы
    def __calculate_s(self):
        for i in range(len(self.m_list)):
            x_list = copy.copy(self.m_list[i][0])
            x_list.insert(0, 1)
            s = self.neuron.calculate_s(x_list)
            self.s_list.append(s)
            print(self.m_list[i][2] + ', s = ' + str(s))

    def __calculate_gemini(self):
        a1 = self.__help_gemini(self.letter_c, self.letter_a1)
        print('А1 + С: ' + str(a1))
        a2 = self.__help_gemini(self.letter_c, self.letter_a2)
        print('А2 + С: ' + str(a2))
        b1 = self.__help_gemini(self.letter_c, self.letter_b1)
        print('B1 + С: ' + str(b1))
        b2 = self.__help_gemini(self.letter_c, self.letter_b2)
        print('B2 + С: ' + str(b2))

    # Подсчёт схожести
    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def __avg_divider(self):
        tmp = 0
        for i in range(len(self.s_list)):
            tmp += self.s_list[i]
        result = tmp / len(self.s_list)
        self.divider = result