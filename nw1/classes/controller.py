from classes.calculating import Calculating
from classes.functions import ActivationFunctionConst

class Controller:
    def __init__(self):
        self.algorithm = Calculating()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_a1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_a2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_b1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_b2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c(self, matrix):
        self.algorithm.letter_c = [0 if not el else 1 for line in matrix for el in line]

    def read_function(self, name_func):
        t = ActivationFunctionConst()
        if name_func == 'Биполярная':
            self.algorithm.act_func = t.bipolar_function
        elif name_func == 'Бинарная':
            self.algorithm.act_func = t.binary_function
        else:
            self.algorithm.act_func = t.bipolar_function

    def teach_neuron(self):
        self.algorithm.teaching()

    def recognize(self):
        return self.algorithm.recognize()
