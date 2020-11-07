def gamma_correction(self, uvh_array, nyt, element):
    s = 'UвхR = ' + str(uvh_array) + '\n'
    current_w = copy.copy(self.a_r_matrix)  # начальные веса
    s += 'Начальные веса: ' + str(current_w) + '\n'
    uvr1 = uvh_array[0]
    uvr2 = uvh_array[1]
    summuvr = uvr1 + uvr2
    s += 'Сумма UвхR = ' + str(summuvr) + '\n'
    print(s)
    l = 0
    flag = False
    dw_array = copy.copy(current_w)
    while not flag:  # цикл по тешкам
        k = l + 1
        print('t' + str(k).translate(self.SUB) + ':\n')
        el = element[0] if l % 2 == 0 else element[1]
        index_array = [i for i in range(len(el)) if el[i] == 1]
        n = len(self.a_array)
        nak = numpy.sum(el)
        ny = nyt

        l += 1


def calculate_dw(self, index_array, n, nak, ny, dw_array, el):
    i = 1
    dw_current = -self.delta_w(ny, nak, n, True) if i in index_array else self.delta_w(ny, nak, n, False)
    check_dw, flg = self.check_dw(dw_array[i - 1], dw_current)
    if flg:
        dw_current = -self.delta_w_with_flag(ny, nak, n, True) if i in index_array else self.delta_w(ny, nak, n, False)

    dw_array.append(dw_current)
    i += 1
    calc_delta_w = self.delta_w_with_flag if flg else self.delta_w
    while i < len(el):
        dw_current = -calc_delta_w(ny, nak, n, True) if i in index_array else calc_delta_w(ny, nak, n, False)

        i += 1


def check_dw(self, dw_last, dw_current):
    tmp = 1 - dw_last
    return (numpy.abs(dw_current - dw_last), True) if dw_current > tmp else (dw_current, False)