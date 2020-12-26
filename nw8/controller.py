from alorithm import *


class Controller:
    def __init__(self):
        self.algorithm = Algorithm()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_3 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_4 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_c1(self, matrix):
        self.algorithm.letter_5 = [-1 if not el else 1 for line in matrix for el in line]



    def read_letter_c2(self, matrix):
        self.algorithm.letter_6 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_d1(self, matrix):
        self.algorithm.letter_7 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_d2(self, matrix):
        self.algorithm.letter_8 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_e1(self, matrix):
        self.algorithm.letter_9 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_e2(self, matrix):
        self.algorithm.letter_0 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_rs(self, matrix):
        self.algorithm.letter_r = [-1 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self):
        self.algorithm.teaching()

    # def recognize(self):
    #     return self.algorithm.recognize()
