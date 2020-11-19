from calculate.utils import *
from l53.newuron_web_mor import NeuronWebMor


class CalculatingMor:
    def __init__(self):
        self.letter_a1 = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
        self.letter_a2 = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
        self.letter_b1 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        self.letter_b2 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
        self.letter_c1 = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.letter_c2 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.letter_d1 = [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        self.letter_d2 = [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        self.letter_e1 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1]
        self.letter_e2 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]
        self.letter_rs = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1]
        self.m_list = None
        self.neuron_web = None
        self.rs = None

    def recognize(self):
        print('\n>> РАСПОЗНАВАНИЕ...')
        print('\n>> Буква для распознавания')
        self.__make_rs_list_binary()
        print('\n>> Подсчет схожести')
        self.__calculate_gemini()
        self.neuron_web.recognize(self.rs)
        return [1]

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

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def __make_rs_list_binary(self):
        if self.letter_rs is not None:
            rs = copy_and_insert_one(self.letter_rs)
            print(rs)
            self.rs = rs

    def teaching(self, count_hide=2):
        print('\n>> ОБУЧЕНИЕ...')
        self.__make_letters_list()
        print('\n>> Создание обучающих выборок')
        self.m_list = self.__make_all_m()
        print('\n>> Создание НС')
        self.neuron_web = NeuronWebMor(len(self.letter_a1), len(self.letters_list), count_hide)
        print(self.neuron_web)
        print('\n>> НАЧАЛО ОБУЧЕНИЯ С ПОМОЩЬЮ МОР...')
        self.neuron_web.teaching(self.m_list, 0.1)

    def __make_letters_list(self):
        self.letters_list = [
            (self.letter_a1, self.letter_a2),
            (self.letter_b1, self.letter_b2)]
        if self.letter_c1 is not None and self.letter_c2 is not None:
            self.letters_list.append((self.letter_c1, self.letter_c2))
        if self.letter_d1 is not None and self.letter_d2 is not None:
            self.letters_list.append((self.letter_d1, self.letter_d2))
        if self.letter_e1 is not None and self.letter_e2 is not None:
            self.letters_list.append((self.letter_e1, self.letter_e2))

    def __make_all_m(self):
        def __upd_binary_list(letters_list):
            result = []
            for el in letters_list:
                tmp1 = copy_and_insert_one(el[0])
                tmp2 = copy_and_insert_one(el[1])
                result.append((tmp1, tmp2))
            return result

        letters = __upd_binary_list(self.letters_list)
        y = [0 for _ in range(len(letters))]
        res = []

        for i in range(len(letters)):
            new_y = copy.copy(y)
            new_y[i] = 1
            res.append((letters[i][0], new_y))
            res.append((letters[i][1], new_y))
        return res
