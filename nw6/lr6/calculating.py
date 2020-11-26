import copy


class CalculatingMor:
    def __init__(self):
        # self.letter_a1 = [-1, 1, -1, -1, 1, -1, -1, 1, -1]
        # self.letter_b1 = [1, 1, 1, 1, -1, 1, 1, -1, 1]
        # self.letter_c1 = [1, -1, 1, 1, 1, 1, 1, -1, 1]
        # self.letter_d1 = [1, 1, 1, 1, -1, -1, 1, -1, -1]
        # self.letter_e1 = [-1, -1, -1, -1, 1, -1, -1, -1, -1]
        # self.letter_rs = [-1, -1, 1, 1, 1, 1, 1, -1, 1]
        self.letter_a1 = [1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, -1, 1]
        self.letter_a2 = [1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1]
        self.letter_b1 = [1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1]
        self.letter_b2 = [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, -1]
        self.letter_c1 = [-1, -1, 1, -1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1]
        self.letter_c2 = [-1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1]
        self.letter_d1 = [1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]
        self.letter_d2 = [1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, -1, -1]
        self.letter_e1 = [1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1]
        self.letter_e2 = [1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, -1, 1, 1]
        self.letter_rs = [1, -1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, -1, 1, 1]
        self.letters_list = None
        self.ws_matrix = None
        self.b = None
        self.k = None
        self.un = None
        self.eps = None
        self.z_list = None
        self.a_list = None
        self.y_list = None

    def __activate_z__(self, uvh):
        if uvh <= 0:
            return 0
        elif 0 <= uvh <= self.un:
            return self.k * uvh
        else:
            return self.un

    def __activate_a__(self, uvh):
        if uvh > 0:
            return uvh
        else:
            return 0.0

    def __activate_y__(self, uvh):
        return 1.0 if uvh > 0.0 else 0.0

    def teaching(self):
        print('\n>> ОБУЧЕНИЕ...')
        # self.letters_list = [
        #     (self.letter_a1, self.letter_a2),
        #     (self.letter_b1, self.letter_b2),
        #     (self.letter_c1, self.letter_c2),
        #     (self.letter_d1, self.letter_d2),
        #     (self.letter_e1, self.letter_e2)
        # ]
        self.letters_list = [self.letter_a1, self.letter_b1, self.letter_c1, self.letter_d1, self.letter_e1]
        self.ws_matrix = [[float(el / 2) for el in letter] for letter in self.letters_list]
        print('Матрица весов (строки - V-элементы, столбцы - S): ')
        for ws_list in self.ws_matrix:
            for w in ws_list:
                print('{0:8}'.format(str(w)), end='')
            print()
        self.b = len(self.letter_a1) / 2
        print('Смещения. m/2 = ' + str(len(self.letter_a1)) + '/2 = ' + str(self.b))

    def recognize(self, k=0.01):
        print('\n>> РАСПОЗНАВАНИЕ...')
        self.__calculate_gemini()
        self.k = k
        self.eps = 1 / len(self.letters_list)
        self.un = 1 / self.k
        print('k = ' + str(k))
        print('un = ' + str(self.un))
        print('eps = ' + str(self.eps))
        lst_vh = []
        for ws_list in self.ws_matrix:
            tmp = [ws_list[i] * self.letter_rs[i] for i in range(len(ws_list))]
            s = sum(tmp)
            s += self.b
            lst_vh.append(round(s, 4))
        print('Список Uвх(z) = ' + str(lst_vh))
        lst_vih = []
        for vh in lst_vh:
            tmp = self.__activate_z__(vh)
            lst_vih.append(round(tmp, 4))
        print('Список Uвых(z) = ' + str(lst_vih))
        current_lst_a = self.__calc_a_t(lst_vih, 0)
        for i in range(1, len(self.letters_list)):
            new_lst_a = self.__calc_a_t(current_lst_a, i)
            if new_lst_a == current_lst_a:
                current_lst_a = copy.copy(new_lst_a)
                break
            current_lst_a = copy.copy(new_lst_a)
        print('Список Uвых(A) на последнем шаге = ' + str(current_lst_a))
        answer = []
        for el in current_lst_a:
            answ = self.__activate_y__(el)
            answer.append(answ)
        print('Ответ: ' + str(answer))

    def __calc_a_t(self, lst_vih, index):
        lst_a = []
        count = 0
        for i in range(len(lst_vih)):
            a = lst_vih[count]
            lst = [lst_vih[j] for j in range(len(lst_vih)) if j != count]
            s = round(sum(lst), 4)
            tmp = round((a - self.eps * s), 4)
            answer = self.__activate_a__(tmp)
            lst_a.append(answer)
            count += 1
        print('Список Uвых(A' + str(index) + ') = ' + str(lst_a))
        return lst_a

    def __calculate_gemini(self):
        print('Схожесть... ')
        maximum = 0
        index = 0
        for i in range(len(self.letters_list)):
            j = i + 1
            s = 'Буква №' + str(j) + ': '
            letter = self.letters_list[i]  # [0]
            tmp1 = self.__help_gemini(self.letter_rs, letter)
            s += str(tmp1)
            # letter = copy_and_insert_one(self.letters_list[i][1])
            # tmp2 = self.__help_gemini(self.rs, letter)
            # s += str(tmp2)
            max_tmp = tmp1  # + tmp2
            if max_tmp >= maximum:
                maximum = max_tmp
                index = i
            print(s)
        print('Предположительно rs похожа на букву №' + str(index + 1))

    def __help_gemini(self, letter_a, letter_b):
        t = 0
        for i in range(len(letter_a)):
            if letter_b[i] == letter_a[i]:
                t += 1
        return t
