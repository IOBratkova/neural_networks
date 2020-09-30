from classes.functions import ActivationFunctionConst
from classes.calculating import Calculating


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
        if name_func is None:
            self.algorithm.act_func = ActivationFunctionConst.binary
        elif name_func == 'Бинарная':
            self.algorithm.act_func = ActivationFunctionConst.binary
        elif name_func == 'Биполярная':
            self.algorithm.act_func = ActivationFunctionConst.bipolar


    def teach_neuron(self):
        self.algorithm.calculate()
