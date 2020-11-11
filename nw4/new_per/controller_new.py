from new_per.perseptron_calculating import Calculating


class Controller:
    def __init__(self):
        self.algorithm = Calculating()

    def read_letter_a1(self, matrix):
        self.algorithm.letter_a1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b1(self, matrix,):
        self.algorithm.letter_b1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_a2(self, matrix):
        self.algorithm.letter_a2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_b2(self, matrix, ):
        self.algorithm.letter_b2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c1(self, matrix):
        self.algorithm.letter_c1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_c2(self, matrix,):
        self.algorithm.letter_c2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_r1(self, matrix):
        self.algorithm.letter_r1 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_r2(self, matrix):
        self.algorithm.letter_r2 = [0 if not el else 1 for line in matrix for el in line]

    def read_letter_r3(self, matrix):
        self.algorithm.letter_r3 = [0 if not el else 1 for line in matrix for el in line]

    def teach_neuron(self, w_range, a_count):
        # TODO: СМОТРИ НИЖЕ
        # Добавить диапазон весовых коэффициентов
        # Добавить кол-во нейронов А-слоя
        # w_range = (0.0, 1.0)
        # a_count = 12
        self.algorithm.teaching(w_range, a_count)

    def recognize(self):
        return self.algorithm.recognition()
