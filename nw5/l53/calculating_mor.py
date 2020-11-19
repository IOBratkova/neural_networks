from calculate.utils import *
from l53.newuron_web_mor import NeuronWebMor


class CalculatingMor:
    def __init__(self):
        self.letter_a1 = None
        self.letter_a2 = None
        self.letter_b1 = None
        self.letter_b2 = None
        self.letter_rs = None
        self.m_list = None

    def teaching(self, count_hide=2):
        print('\n>> ОБУЧЕНИЕ...')
        self.__make_letters_list()
        print('\n>> Создание обучающих выборок')
        self.m_list = self.__make_all_m()
        print('\n>> Создание НС')
        neuron_web = NeuronWebMor(len(self.letter_a1), len(self.letters_list), count_hide)
        print(neuron_web)
        print('\n>> НАЧАЛО ОБУЧЕНИЯ С ПОМОЩЬЮ МОР...')
        neuron_web.teaching(self.m_list, 0.5, 100)

    def __make_letters_list(self):
        self.letters_list = [
            (self.letter_a1, self.letter_a2),
            (self.letter_b1, self.letter_b2)]

    def __make_all_m(self):
        def __upd_binary_list():
            result = []
            for el in self.letters_list:
                tmp1 = copy_and_insert_one(el[0])
                tmp2 = copy_and_insert_one(el[1])
                result.append(tmp1)
                result.append(tmp2)
            return result

        def __make_m(index):
            result = []
            lst = __upd_binary_list()
            i = 0
            while i < len(lst):
                if i == index or i == index + 1:
                    tmp = lst[i], [1, 0]
                    print(tmp)
                    result.append(tmp)
                else:
                    tmp = lst[i], [0, 1]
                    print(tmp)
                    result.append(tmp)
                i += 1
            return result

        res = __make_m(0)
        # for el in self.letters_list:
        #
        # for i in range(len(self.letters_list)):
        #     j = i+1
        #     print('m-' + str(j))
        #     tmp = __make_m(i)
        #     res.append(tmp)
        return res