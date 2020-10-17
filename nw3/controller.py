
from calculate.calculating import Calculator
from calculate.functions import ActivationFunctionConst


class Controller:
    def __init__(self):
        self.algorithm = Calculator()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_a1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_a2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_b1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_b2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c1(self, matrix):
        self.algorithm.letter_c1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c2(self, matrix):
        self.algorithm.letter_c2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_d1(self, matrix):
        self.algorithm.letter_d1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_d2(self, matrix):
        self.algorithm.letter_d2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_e1(self, matrix):
        self.algorithm.letter_e1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_e2(self, matrix):
        self.algorithm.letter_e2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_rs(self, matrix):
        self.algorithm.letter_rs = [0 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self, value_k, value_alpha):
        self.algorithm.k = value_k
        self.algorithm.alpha = value_alpha
        self.algorithm.teaching()

    def recognize(self):
        return self.algorithm.recognition()

    def read_function(self, name_func):
        t = ActivationFunctionConst()
        if name_func == 'Биполярная':
            self.algorithm.act_func = t.bipolar_function
        elif name_func == 'Бинарная':
            self.algorithm.act_func = t.binary_function
        elif name_func == 'Сигмоидальная':
            self.algorithm.act_func = t.sigmoid_function
        elif name_func == 'D-правило, биполяр.':
            self.algorithm.act_func = t.bipolar_delta_function
        else:
            self.algorithm.act_func = t.bipolar_function
