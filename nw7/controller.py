
from l7.calculatting import CalculatingMor


class Controller:
    def __init__(self):
        self.algorithm = CalculatingMor()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_3 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_4 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c1(self, matrix):
        self.algorithm.letter_5 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c2(self, matrix):
        self.algorithm.letter_6 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_d1(self, matrix):
        self.algorithm.letter_7 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_d2(self, matrix):
        self.algorithm.letter_8 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_e1(self, matrix):
        self.algorithm.letter_9 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_e2(self, matrix):
        self.algorithm.letter_0 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_rs(self, matrix):
        self.algorithm.letter_rs = [0 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self):
        # print('Чтобы запустить тестовый пример, нажмите 1\n')
        # t = int(input())
        # if t == 1:
        #     self.algorithm.teaching()
        # else:
        self.algorithm.teaching(False)

    def recognize(self):
        return self.algorithm.recognize()
