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

    def gamma_correction2(self, uvh_array, nyt, element, teta):
        current_w = copy.copy(self.a_r_matrix)
        uvr1 = uvh_array[0]
        uvr2 = uvh_array[1]
        summuvr = uvr1 + uvr2
        s = 'UвхR = ' + str(uvh_array) + '\n'
        s += 'Начальные веса: ' + str(current_w) + '\n'
        s += 'Сумма UвхR = ' + str(summuvr) + '\n'
        print(s)
        l = 0
        flag = False
        not_update_w = []

        while not flag:
            k = l + 1
            print('t' + str(k).translate(self.SUB) + ':\n')
            activ = self.select_element(teta, uvh_array, l)
            if activ is None:
                print('канец')
                return
            current_w, not_update_w = self.calc_dw(element[activ], nyt, not_update_w, current_w)
            #current_w = [current_w[i] + dw[i] for i in range(len(current_w))]
            self.a_r_matrix = current_w
            # self.calc_Ilia(element[activ], self.a_r_matrix, nyt)
            uvh_array[activ] = self.u_input_r(element[activ])
            #uvh_array = [self.u_input_r(element[i]) for i in range(len(element))]
            s = 'Сумма UвхR = ' + str(numpy.sum(self.a_r_matrix)) + '\n'
            print(s)
            l += 1

        def calc_dw(self, index_array, ny, not_update_w, current_w):
            dw_array = []
            lent = len(self.a_r_matrix)
            active = []
            passive = []
            for i in range(len(index_array)):
                if index_array[i] == 1:
                    active.append(i)
                else:
                    passive.append(i)
            n = len(index_array)
            nak = len(active)
            i = 0
            dw = -self.delta_w(ny, nak, n, True) if i in index_array else self.delta_w(ny, nak, n, False)
            dw, fl = self.help_calc_delta_w(self.a_r_matrix[0], dw)
            func = self.delta_w
            if fl:
                func = self.delta_w_with_flag
                not_update_w.append(i)
            dw_array.append(dw)
            i += 1
            while i < lent:
                fl = False
                if i not in not_update_w:
                    dw = -func(ny, nak, n, True) if i in index_array else func(ny, nak, n, False)
                    ch, fl = self.help_calc_delta_w(self.a_r_matrix[i], dw)
                    dw = ch
                if fl:
                    not_update_w.append(i)
                    func = self.delta_w_with_flag
                dw_array.append(dw)
                i += 1

            for index in active:
                current_w[index] += dw * len(passive) / (len(current_w))

            for index in passive:
                current_w[index] -= dw * len(active) / (len(current_w))

            return current_w, not_update_w

            # Вернет разность и значение Тистина, если нужно юзать с этого моммента другой способ вычислений

        def help_calc_delta_w(self, w_last, dw_current):
            tmp = 1 - w_last
            tmp2 = numpy.abs(dw_current - w_last)
            if dw_current > tmp:
                return (tmp2, True)
            else:
                return (dw_current, False)
            # return (tmp2, True) if dw_current > tmp else (dw_current, False)

        def gamma_correction3(self, uvh_array, nyt, element, teta):
            current_w = copy.copy(self.a_r_matrix)
            current_w = [round(c, 2) for c in current_w]
            uvr1 = uvh_array[0]
            uvr2 = uvh_array[1]
            summuvr = uvr1 + uvr2
            s = 'UвхR = ' + str(uvh_array) + '\n'
            s += 'Начальные веса: ' + str(current_w) + '\n'
            s += 'Сумма UвхR = ' + str(summuvr) + '\n'
            print(s)
            l = 0
            flag = False
            not_update_w0 = []
            while not flag:
                k = l + 1
                print('t' + str(k).translate(self.SUB) + ':\n')
                activ = self.select_element(teta, uvh_array, l)
                if activ is None:
                    print('канец')
                    return
                tmp, tmp2 = self.calculate_delta_w_list(current_w, not_update_w0, element[activ], nyt)
                not_update_w0 = copy.copy(tmp2)
                current_w = copy.copy(tmp)
                self.a_r_matrix = copy.copy(tmp)
                uvh_array[activ] = self.u_input_r(element[activ])

                ssuumm = numpy.sum(self.a_r_matrix)
                ssuumm += uvh_array[activ]

                # uvh_array = [self.u_input_r(element[i]) for i in range(len(element))]
                s = 'Сумма UвхR = ' + str(numpy.sum(current_w)) + '\n'
                print(s)
                print(ssuumm)
                l += 1

        def calculate_delta_w_list(self, current_w, not_update_w, index_array, nya):
            eps = 1e-7
            active = []
            passive = []
            for i in range(len(index_array)):
                if i not in not_update_w:
                    if index_array[i] == 1:
                        active.append(i)
                    else:
                        passive.append(i)

            func = self.delta_w  # if len(not_update_w) == 0 else self.delta_w_with_flag
            dws = []

            ws = copy.copy(current_w)
            for i in range(len(current_w)):
                dw = 0.0
                if i not in not_update_w:
                    dw = func(nya, len(active), len(index_array), False) if i in passive else func(nya, len(active),
                                                                                                   len(index_array),
                                                                                                   True)
                    dw, fl = self.help_calc_delta_w(ws[i], dw)
                    if fl:
                        if i not in not_update_w:
                            not_update_w.append(i)
                        # func = self.delta_w_with_flag
                dws.append(round(dw, 2))

            for i in range(len(current_w)):
                if i in active:
                    current_w[i] -= dws[i]
                if i in passive:
                    current_w[i] += dws[i]

                current_w[i] = round(current_w[i], 2)

                if current_w[i] <= 0.0:
                    current_w[i] = 0.0
                    if i not in not_update_w:
                        not_update_w.append(i)
                if current_w[i] >= 1.0:
                    current_w[i] = 1.0
                    if i not in not_update_w:
                        not_update_w.append(i)

            # current_w = [round(c, 2) for c in current_w]
            print(numpy.sum(current_w))

            return current_w, not_update_w