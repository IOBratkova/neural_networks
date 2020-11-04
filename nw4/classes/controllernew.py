from classes.calculatingnew import Calculating


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

    def read_letter_c1(self, matrix):
        self.algorithm.letter_c1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c2(self, matrix):
        self.algorithm.letter_c2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c3(self, matrix):
        self.algorithm.letter_c3 = [0 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self):
        # TODO: СМОТРИ НИЖЕ
        # Добавить диапазон весовых коэффициентов
        # Добавить кол-во нейронов А-слоя
        self.algorithm.teaching()

    def recognize(self):
        return self.algorithm.recognition()
