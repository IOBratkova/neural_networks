
from lr6.calculating import CalculatingMor


class Controller:
    def __init__(self):
        self.algorithm = CalculatingMor()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_a1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_a2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_b1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_b2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_c1(self, matrix):
        self.algorithm.letter_c1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_c2(self, matrix):
        self.algorithm.letter_c2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_d1(self, matrix):
        self.algorithm.letter_d1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_d2(self, matrix):
        self.algorithm.letter_d2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_e1(self, matrix):
        self.algorithm.letter_e1 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_e2(self, matrix):
        self.algorithm.letter_e2 = [-1 if not el else 1 for line in matrix for el in line]

    def read_letter_rs(self, matrix):
        self.algorithm.letter_rs = [-1 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self):
        self.algorithm.teaching()

    def recognize(self):
        return self.algorithm.recognize()
