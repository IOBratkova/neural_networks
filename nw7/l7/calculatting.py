import random
import numpy as nym
import copy

class CalculatingMor:
    def __init__(self):
        self.letter_1 = [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]
        self.letter_2 = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
        self.letter_3 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
        self.letter_4 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0]
        self.letter_5 = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.letter_6 = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1]
        self.letter_7 = [1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        self.letter_8 = [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
        self.letter_9 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1]
        self.letter_0 = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1]
        self.letter_rs = [1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1]
        self.m = None
        self.alpha = 0.9
        self.k = 0.1
        self.w_matrix = None
        self.recognize_matrix = None
        self.a_list = None
        self.letters_list = None
        self.eps = 0.0001
        self.dictionary = None

    def teaching(self, flag=True):
        print('>> ОБУЧЕНИЕ....')
        self.__create_start_data__(flag)
        flag = False
        matrix_a = copy.copy(self.w_matrix)
        alpha = copy.copy(self.alpha)
        iterate = 1
        while not flag:
            print('\n==============Итерация №' + str(iterate) +'==============', end='')
            tmp_matrix = copy.deepcopy(matrix_a)
            for i in range(len(self.letters_list)):
                j = i + 1
                print('\nСимвол №' + str(j) + ': ' + str(self.letters_list[i]))
                win_index = self.__calc_d__(self.letters_list[i], tmp_matrix)
                tmp_matrix = self.__calc_w_new__(win_index, tmp_matrix, self.letters_list[i], alpha)
                print('\nВеса: ')
                for el in tmp_matrix:
                    print(el)
            alpha = alpha * self.k
            matrix_b = copy.copy(tmp_matrix)
            flag = self.__sub_eps__(matrix_a, matrix_b)
            iterate += 1
            print('\nЗНАЧЕНИЕ ВЕСОВ В КОНЦЕ ЭТОЙ ИТЕРАЦИИ: ')
            for el in tmp_matrix:
                print(el)
            print('Значение alpha после коррекции, aplha = ' + str(alpha))
            matrix_a = copy.copy(matrix_b)
            print('=====================================')
        res_matr = copy.copy(matrix_a)

        print('\nПоследняя матрица весов (с округлением до 2 символов): ')
        res_matr2 = [[round(r, 2) for r in row] for row in res_matr]
        for el in res_matr2:
            print(el)
        self.w_matrix = copy.deepcopy(matrix_a)
        self.classified()
        print('Итераций всего ' + str(iterate))

    def classified(self):
        print('\n>> КЛАССИФИКАЦИЯ....')
        print('нумерация с 0')
        dictionary = {}
        classes = []
        tmp_matrix = copy.deepcopy(self.w_matrix)
        i = 0
        for letter in self.letters_list:
            a = nym.array([letter])
            b = nym.array(tmp_matrix)
            total = a.dot(b)
            array = total.tolist()
            array0 = array[0]
            index = array0.index(max(array0))
            print('Изображение ' + str(i) + ': ' + str(letter) + ', отнесено к классу: ' + str(index))
            if index not in classes:
                classes.append(index)
            if index not in dictionary:
                dictionary[index] = []
                dictionary[index].append(i)
            else:
                dictionary[index].append(i)
            i += 1
        classes.sort()
        print(dictionary)
        self.dictionary = dictionary
        print('Обнаружены классы: ' + str(classes))
        del_classes = []
        for i in range(len(self.letters_list)):
            if i not in classes:
                del_classes.append(i)
        del_classes.reverse()
        print('Не обнаруженные классы: ' + str(del_classes))
        for index in del_classes:
            for row in tmp_matrix:
                del row[index]
        res_matrix = [[round(r, 2) for r in row] for row in tmp_matrix]
        for el in res_matrix:
            print(el)
        print()
        sorted(self.dictionary.keys())
        self.recognize_matrix = copy.deepcopy(tmp_matrix)
        print(self.dictionary)

    def recognize(self):
        print('\n>> РАСПОЗНАВАНИЕ....')
        self.__calculate_gemini()
        a = nym.array([self.letter_rs])
        b = nym.array(self.recognize_matrix)
        total = a.dot(b)
        array = total.tolist()
        array = array[0]
        print(self.dictionary)
        print(array)

    def __calculate_gemini(self):
        print('Схожесть... ')
        maximum = 0
        index = 0
        i = 0
        for key, value in self.dictionary.items():
            s = 'Класс №' + str(key) + ': '
            summa = 0
            for el in value:
                letter = self.letters_list[el]
                summa += self.__help_gemini(self.letter_rs, letter)
            s += str(summa)
            if summa >= maximum:
                maximum = summa
                index = key
            print(s)
            i += 1
        print('Предположительно rs класс №' + str(index))

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t

    def __calc_d__(self, letter, matrix):
        ds = []
        for j in range(self.m): #по кол-ву A-элементов
            d = sum([((matrix[i][j] - letter[i]) ** 2) for i in range(len(letter))])
            ds.append(d)
        index = ds.index(min(ds))
        jndex = copy.copy(index) + 1
        print(str(ds) + '\nПобедил элемент №' + str(jndex) + ' = ' + str(ds[index]))
        return index

    def __calc_w_new__(self, index, matrix, letter, alpha):
        tmp_matrix = copy.deepcopy(matrix)
        for i in range(len(letter)):
            w_old = float(tmp_matrix[i][index])
            letter_w_old = letter[i] - w_old
            letter_w_old *= alpha
            w_new = w_old + letter_w_old
            tmp_matrix[i][index] = copy.deepcopy(w_new)
        return tmp_matrix

    def __sub_eps__(self, matrix_a, matrix_b):
        a = nym.array(matrix_a)
        b = nym.array(matrix_b)
        c = a - b
        for el in c:
            for e in el:
                if nym.fabs(e) > self.eps:
                    return False
        return True

    def __sub_matrix__(self, a, b):
        pass


    def __make_letters_list(self):
        self.letters_list = []
        if self.letter_1 is not None:
            self.letters_list.append(self.letter_1)
        if self.letter_2 is not None:
            self.letters_list.append(self.letter_2)
        if self.letter_3 is not None:
            self.letters_list.append(self.letter_3)
        if self.letter_4 is not None:
            self.letters_list.append(self.letter_4)
        if self.letter_5 is not None:
            self.letters_list.append(self.letter_5)
        if self.letter_6 is not None:
            self.letters_list.append(self.letter_6)
        if self.letter_7 is not None:
            self.letters_list.append(self.letter_7)
        if self.letter_8 is not None:
            self.letters_list.append(self.letter_8)
        if self.letter_9 is not None:
            self.letters_list.append(self.letter_9)
        if self.letter_0 is not None:
            self.letters_list.append(self.letter_0)

    def __create_start_data__(self, flag):
        if not flag:
            self.m = 10
            self.__make_letters_list()
            self.w_matrix = [[random.uniform(-0.9, 1.8) for j in range(self.m)] for i in range(len(self.letters_list[0]))]
        else:
            self.letter_0 = [0, 0, 0, 1]
            self.letter_1 = [0, 0, 1, 1]
            self.letter_2 = [1, 0, 0, 0]
            self.letter_3 = [1, 1, 0, 0]
            self.letter_4 = None
            self.letter_5 = None
            self.letter_6 = None
            self.letter_7 = None
            self.letter_8 = None
            self.letter_9 = None
            self.m = 2
            self.a_list = [0 for _ in range(self.m)]
            self.__make_letters_list()
            self.w_matrix = [
                [0.7, 0.6],
                [0.4, 0.1],
                [0.5, 0.5],
                [0.2, 0.9]
            ]
        # self.alpha = 0.6
        print('Буквы: ')
        for el in self.letters_list:
            print(el)
        print('\nВеса: ')
        for el in self.w_matrix:
            print(el)
