import copy

class Calculating:
    def __init__(self):
        self.act_func = None
        self.letter_a1 = None
        self.letter_a2 = None
        self.letter_b1 = None
        self.letter_b2 = None
        self.letter_c = None
        self.neuron = None
        self.m = None

    def make_m(self):
        if self.act_func[0] == 'Бинарная':
            self.m = self.__make_m_by_binary()
        elif self.act_func[0] == 'Биполярная':
            self.m = self.__make_m_by_bipolar()

    def __make_m_by_binary(self):
        return [(self.letter_a1, 1), (self.letter_a2, 1), (self.letter_b1, 0), (self.letter_b2, 0)]

    def __make_m_by_bipolar(self):
        a1 = [0 if not el else 1 for el in self.letter_a1]
        a2 = [0 if not el else 1 for el in self.letter_a2]
        b1 = [0 if not el else 1 for el in self.letter_b1]
        b2 = [0 if not el else 1 for el in self.letter_b2]
        return [(a1, 1), (a2, 1), (b1, 0), (b2, 0)]
