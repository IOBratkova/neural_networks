from calculate.neuron import Neuron
import random
import math
import copy


class Adaline(Neuron):
    def __init__(self, function, count_input, alpha=0.1):
        super().__init__(function, count_input)
        self.w_list = None
        self.w_list = [random.uniform(-0.01, 0.01) for _ in range(count_input)]
        self.w_list_old = copy.copy(self.w_list)
        self.alpha = alpha

    def calculate_u_input(self, x_list):
        new_x_list = [x_list[i] for i in range(len(x_list)) if i != 0]
        new_w_list = [self.w_list[i] for i in range(len(self.w_list)) if i != 0]
        tmp_list = [new_x_list[i] * new_w_list[i] for i in range(len(new_x_list))]
        tmp_list.insert(0, self.w_list[0])
        s = sum(tmp_list)
        return sum(tmp_list)

    def check_stop_rule(self, epsilon=0.01):
        tmp_list = [math.fabs(self.w_list[i] - self.w_list_old[i]) for i in range(len(self.w_list))]
        s = sum(tmp_list)
        flag = s <= epsilon
        return flag, s

    def __correction_w_with_adaline(self, w_old, u_in, u_out, x):
        w_old2 = float(copy.copy(w_old))
        u_in2 = float(copy.copy(u_in))
        u_out2 = float(copy.copy(u_out))
        x2 = float(copy.copy(x))
        alpha2 = float(copy.copy(self.alpha))
        t = u_out2 - u_in2
        m = t * x2
        z = m * alpha2
        s = z + w_old2
        return s

    def correction_w_list_with_adaline(self, x_list, u_out):
        u_in = self.calculate_u_input(x_list)
        print('\nUвх = ' + str(u_in))
        for i in range(len(self.w_list)):
            res = self.__correction_w_with_adaline(self.w_list[i], u_in, u_out, x_list[i])
            self.w_list[i] = copy.copy(float(res))
        print(self.w_list)
