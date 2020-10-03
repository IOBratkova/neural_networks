import copy


class Neuron:
    def __init__(self, function, count_input, count_output=1):
        self.count_input = count_input
        self.count_output = count_output
        self.w_list = [0 for _ in range(count_input)]
        self.function = function

    # Возвращает значение входного суммарного сигнала для x_list на основе весовых коэффициентов w_list
    def calculate_s(self, x_list):
        res = 0
        for i in range(self.count_input):
            res += x_list[i] * self.w_list[i]
        return res

    # Корректировка весовых коэффициентов для x_list со значением y и коэффициентом плавности k
    def correction_w_list(self, x_list, y, k):
        for i in range(len(self.w_list)):
            res = self.__correction_w(self.w_list[i], x_list[i], y, k)
            self.w_list[i] = copy.copy(res)
        print(self.w_list)

    # Подсчет значения w для x и y с указанным k с помощью заранее определенной функции активации
    def __correction_w(self, w, x, y, k):
        return self.function[2](w, x, y, k)
