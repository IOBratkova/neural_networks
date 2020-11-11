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
        self.m_c = None
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
        self.c_s = None
        self.ex_as = None
        self.a_gem = None
        self.b_gem = None

    def teaching(self, w_range, count_a):
        print('\n>> ОБУЧЕНИЕ...')
        print(str((2.664888290944173 + 3.4063565788574324)/2))
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
        self.r_input_signals_teta[0] = self.gamma_correct()

        # a = self.perceptron.u_input_all_a(self.letter_a1[0])
        # b = self.perceptron.u_input_all_a(self.letter_b1[0])
        # tetas = [((a[i] + b[i]) / 2) for i in range(len(a))] #self.threshold_one
        # res1 = [1 if a[i] >= tetas[i] else 0 for i in range(len(tetas))]
        # res2 = [1 if b[i] >= tetas[i] else 0 for i in range(len(tetas))]
        # resRa = self.perceptron.u_input_r(res1)
        # resRb = self.perceptron.u_input_r(res2)
        # teta = (resRa + resRb) / 2
        # self.r_input_signals_teta[0] = teta #
        # print(teta)
        # print(self.r_input_signals_teta[0])
        # print(str(numpy.average([teta, self.r_input_signals_teta[0]])))
        #self.r_input_signals_teta[0] = (teta+self.r_input_signals_teta[0])/2
        print('============!!!=============')


    def recognition(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        self.m_c = None
        self.c_s = None
        self.ex_as = None
        self.c_r = None
        y = None
        self.m_c = copy_and_insert_one(self.letter_c)
        print('\n>> Схожесть буквы С с каждой из буков: ')
        self.__calculate_gemini()
        print('\n>> Входной суммарный сигнал С (A-S), реакция на пороги: ')
        self.c_s, self.ex_as = self.__calculate_w_as()
        print('\n>> Входной суммарный сигнал С (A-R): ')
        self.c_r, y = self.__calculate_w_rs()
        return y

    def __calculate_w_as(self):
        s = self.perceptron.u_input_all_a(self.letter_c)
        tetas = self.threshold_one
        res1 = [1 if s[i] >= self.threshold_one[i] else 0 for i in range(len(tetas))]
        print('teta = ' + str(tetas))
        print('сигнал = ' + str(s))
        print('результат = ' + str(res1))
        return s, res1

    def __calculate_w_rs(self):
        ex_as = self.ex_as
        res = self.perceptron.u_input_r(ex_as)
        print(res)
        #res /= 2
        teta = self.r_input_signals_teta[0]
        y = 1 if res >= teta else -1
        print('teta = ' + str(teta))
        print('сигнал = ' + str(res))
        print('Изображение похоже на класс: ' + str(y))
        return res, y

    def __calculate_gemini(self):
        self.a_gem = self.__help_gemini(self.letter_c, self.letter_a1[0])
        print('А1 + С: ' + str(self.a_gem))
        self.b_gem = self.__help_gemini(self.letter_c, self.letter_b1[0])
        print('B1 + С: ' + str(self.b_gem))

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def gamma_correct(self):
        if len(self.flags) == 0:
            print('Неудачно попрошла настройка.\n'
                  'Нажмите повторно кнопку "Обучить" или введите перед этим новые параметры.')
        else:
            if not self.flags[0]:
                print('Настройка перцептрона по гамма-системе: ')
                return self.gamma_correction()
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
        tmp = numpy.ravel(self.a_inputs_signals)
        mini = numpy.min(tmp)
        maxi = numpy.max(tmp)

        a = self.a_inputs_signals[0]
        b = self.a_inputs_signals[1]
        res = []
        res = [(a[i] + b[i]) / 2 for i in range(len(a))]

        # for i in range(len(a)):
        #     a1 = a[i]
        #     b1 = b[i]
        #     mmini = numpy.min([a1, b1])
        #     mmaxi = numpy.max([a1, b1])
        #     mi2 = numpy.min([mmini, mini])
        #     ma2 = numpy.max([mmaxi, maxi])
        #     res.append((mi2+ma2)/2)

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
        #self.r_input_signals.append(res)
        s = 'Вектор UвхR = ' + str(res)
        teta = (res[0] + res[1])/2
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

        y = True if res < one_tri else False
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
        uvh_array = self.perceptron.gamma_correction(r, 0.1, ta, to)

        res = [self.perceptron.u_input_r(el) for el in self.threshold_array[0][0]]
        maxi1 = numpy.max(uvh_array)
        maxi2 = numpy.max(res)
        t1 = numpy.max([maxi1, maxi2])

        mini1 = numpy.min(uvh_array)
        mini2 = numpy.min(res)
        t2 = numpy.min([mini1, mini2])

        print('старе')
        print(self.r_input_signals_teta)
        self.r_input_signals_teta[0] = t1 #numpy.average([t1, t2])
        print('еове')
        print(self.r_input_signals_teta)
        return t1


