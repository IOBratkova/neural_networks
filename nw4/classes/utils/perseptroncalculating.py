from classes.utils.utils import *
from classes.perceptron.perceptron import Perceptron
import numpy
import copy


class Calculating:
    def __init__(self):
        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.ny = 0.2
        self.letter_a1 = None #[1, 1, 1, 1, 0, 1, 1, 0, 1], 'П'
        self.letter_b1 = None #[1, 0, 1, 1, 1, 1, 1, 0, 1], 'Н'
        self.letter_c = None
        self.letters_array = None  #
        self.m_array = None
        self.input_count = None
        self.perceptron = None
        self.excitatory_neurons = None
        self.a_inputs_signals = None  # UAвх
        self.threshold_array = None
        self.threshold_one = None
        self.threshold_all = None
        self.r_input_signals = None  # URвх
        self.r_input_signals_info = None
        self.r_input_signals_teta = None  # URвх
        self.flags = None

    def teaching(self, w_range, count_a):
        print('\n>> ОБУЧЕНИЕ...')
        self.input_count = len(self.letter_a1[0])
        self.letters_array = [self.letter_a1, self.letter_b1]
        self.m_array = self.make_m_binary()
        print('\nА-элементов = ' + str(count_a))
        print('S-элементов = ' + str(self.input_count))
        print('Диапазон весов = ' + str(w_range) + '\n')
        self.perceptron = Perceptron(self.input_count, count_a, w_range)
#        self.perceptron.print_info()
        self.excitatory_neurons = self.get_excitatory_neurons()
        self.a_inputs_signals = self.get_a_elements_input_signals()
        self.threshold_info()
        self.check_threshold()
        self.get_r_elements_input_signals()
        self.gamma_correct()

    def gamma_correct(self):
        if len(self.flags) == 0:
            print('Неудачно попрошла настройка.\n'
                  'Нажмите повторно кнопку "Обучить" или введите перед этим новые параметры.')
        else:
            if not self.flags[0]:
                print('Настройка перцептрона по гамма-системе: ')
                self.gamma_correction()
            else:
                print('Перецептрон теперь умный и готов что-нибудь распознать!')

    def threshold_info(self):
        self.threshold_all = self.get_threshold_value_for_all()
        self.threshold_one = self.get_threshold_value_for_neurons()

    def get_threshold_value_for_all(self):
        print('\nОбщее пороговое значение: ')
        tmp = numpy.ravel(self.a_inputs_signals)
        s = 'min = '
        mini = numpy.min(tmp)
        s += str(mini) + ', max = '
        maxi = numpy.max(tmp)
        s += str(maxi)
        res = round((mini + maxi) / 2, 1)
        s += '\nПороговое значение, θ = ' + str(res)
        print(s)
        return res

    def get_threshold_value_for_neurons(self):
        print('\nПороговые значения для каждого А-элмента: ')
        a = self.a_inputs_signals[0]
        b = self.a_inputs_signals[1]
        res = [(a[i] + b[i]) / 2 for i in range(len(a))]
        [print('Пороговое значение для A' + str(i).translate(self.SUB) + ', θ = ' + str(res[i])) for i in
         range(len(res))]
        return res

    def get_a_elements_input_signals(self):
        r = [self.perceptron.u_input_all_a(letter[0]) for letter in self.letters_array]
        print('Сигналы на входах А-элементов: ')
        for l in r:
            print(l)
        return r

    def get_r_elements_input_signals(self):
        self.r_input_signals_teta = []
        self.r_input_signals_info = []
        self.r_input_signals = []
        flags = []
        for element in self.threshold_array:
            print(element[1] + ': ')
            res, teta, info = self.check_r(element)
            flag = True if info[0] == self.m_array[0][1] and info[1] == self.m_array[1][1] else False
            print('настройка перцептрона не требуется\n') if flag else print('требуется настройка перцептрона!!\n')
            flags.append(flag)
            self.r_input_signals_teta.append(teta)
            self.r_input_signals_info.append(info)
            self.r_input_signals.append(res)
        self.flags = flags

    def check_r(self, element):
        res = [self.perceptron.u_input_r(el) for el in element[0]]
        self.r_input_signals.append(res)
        s = 'Вектор UвхR = ' + str(res)
        teta = numpy.average(res)
        s += '. Пороговое значение, Rθ = ' + str(teta) + '.\n'
        s += 'Таким образом: ' + str(res[0])
        s += ' >= ' + str(teta)
        s += ' > ' + str(res[1]) + '. '
        info = [1 if res[i] >= teta else -1 for i in range(len(res))]
        s += '\nПри подаче исходных сообщений имеем: ' + str(info)
        s += '. Изначально имеем: ' + str([self.m_array[0][1], self.m_array[1][1]]) + ' => '
        print(s, end='')
        return (res, teta, info)

    def get_excitatory_neurons(self):
        s = '\nВозбуждаемые нейроны, нумерация ведётся с 0: \n'
        res = [(self.perceptron.get_excitatory_neurons(letter[0]), letter[1]) for letter in self.letters_array]
        for r in res:
            s += str(r[1]) + ': '
            s += str(r[0]) + '\n'
        print(s)
        return res

    def check_threshold(self):
        result = [(self.check_threshold_one(), 'Индивидуальные пороги')
                  ,(self.check_threshold_all(), 'Один порог для всех')]
        if result[0] is None and result[1] is None:
            print('Беда...')
        self.threshold_array = [el for el in result if el[0] is not None]

    def check_threshold_one(self):
        print('\nИндивидуальные пороги для А-элементов: ')
        a = self.a_inputs_signals[0]
        b = self.a_inputs_signals[1]
        res1 = [1 if a[i] >= self.threshold_one[i] else 0 for i in range(len(self.threshold_one))]
        res2 = [1 if b[i] >= self.threshold_one[i] else 0 for i in range(len(self.threshold_one))]
        print(str(self.letters_array[0][1]) + ': ' + str(res1))
        print(str(self.letters_array[1][1]) + ': ' + str(res2))
        return [res1, res2] if self.answer_about_teta(res1, res2, 'Индивидуальные пороги для всех нейронов') else None

    def check_threshold_all(self):
        print('\nОдин порог для всех А-элементов: ')
        res1 = [1 if uin >= self.threshold_all else 0 for uin in self.a_inputs_signals[0]]
        res2 = [1 if uin >= self.threshold_all else 0 for uin in self.a_inputs_signals[1]]
        print(str(self.letters_array[0][1]) + ': ' + str(res1))
        print(str(self.letters_array[1][1]) + ': ' + str(res2))
        return [res1, res2] if self.answer_about_teta(res1, res2,
                                                      'Один порог для всех нейронов') else None

    def answer_about_teta(self, res1, res2, info=''):
        res = numpy.sum([1 if res1[i] == res2[i] else 0 for i in range(len(res1))])
        one_tri = self.input_count / 3
        y = True if res == 0 else False
        if y:
            print('Все нейроны реагируют по-разному')
            print('Условие типа \"' + info + '\" удовлетворяет требованиям\n') \
                if y else print('Условие типа \"' + info + '\" _НЕ_ удовлетворяет требованиям\n')
            return y

        y = True if res > one_tri else False
        if y:
            print('Не больше одной трети нейронов реагирует по-разному')
            print('Условие типа \"' + info + '\" удовлетворяет требованиям\n') \
                if y else print('Условие типа \"' + info + '\" _НЕ_ удовлетворяет требованиям\n')
            return y

    def make_m_binary(self):
        result = []
        for i in range(len(self.letters_array)):
            letter = copy_and_insert_one(self.letters_array[i][0])
            y = -1 if i % 2 != 0 else 1
            result.append((letter, y, self.letters_array[i][1]))
            print(result[i])
        return result

    def gamma_correction(self):
        r = copy.copy(self.r_input_signals[0])
        ta = copy.copy(self.threshold_array[0][0])
        to = copy.copy(self.r_input_signals_teta[0])
        self.perceptron.gamma_correction(r, 0.5, ta, to)

    def recognition(self):
        pass
