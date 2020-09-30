import copy

class Neuron:
    def __init__(self, count_input, count_output, x_list, function):
        self.count_input = count_input
        self.count_output = count_output
        self.x_list = x_list  # нахуа он мне
        self.w_list = [0 for _ in range(count_input)]
        self.function = function
        # self.binary_function = ('Бинарная', self.binary, self.hebb_for_binary)
        # self.bipolar_function = ('Биполярная', self.bipolar, self.hebb_for_bipolar)

        # #Функции переехали сюда
        # self.function_dict = {'Биполярная': (lambda x: 1 if x > 0 else 0, lambda w, x, y: w+1 if x==1 and y==1 else
        # w-1 if x!=0 and not y else w if not x else w),
        #                       'Бинарная': (lambda x: 1 if x > 0 else -1, lambda w, x, y: w+x*y)}
        # self.functions_s = [lambda s: 1/(1 + pow(e, -s)), lambda s: 2/(1 + pow(e, -2 * s))-1, lambda s: max(0, s)]

    def z(self, b):
        z = 0
        i = 0
        while i < self.count_input:
            z += self.x_list * self.w_list
        return z + b

    def correction_w_list(self, x, y):
        for i in range(len(self.w_list)):
            res = self.__correction_w(self.w_list[i], x[i], y)
            self.w_list[i] = copy.copy(res)

    def __correction_w(self, w, x, y):
        return self.function[2](w, x, y)
