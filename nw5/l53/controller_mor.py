from l53.calculating_mor import CalculatingMor


class ControllerMor:
    def __init__(self):
        self.algorithm = CalculatingMor()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_a1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_a2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix):
        self.algorithm.letter_b1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix):
        self.algorithm.letter_b2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_rs(self, matrix):
        self.algorithm.letter_rs = [0 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self):
        self.algorithm.teaching()