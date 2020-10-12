import copy
from tkinter import *
from window.grid import MyGrid
from controller import Controller


class MainWindow:
    def __init__(self):
        # Окно0
        self.__window = Tk()
        self.__window.wm_minsize(620, 470)
        self.__controller = Controller()

        # Кнопочки
        self.__button_a1 = None
        self.__button_a2 = None
        self.__button_b1 = None
        self.__button_b2 = None
        self.__button_c1 = None
        self.__button_c2 = None
        self.__button_d1 = None
        self.__button_d2 = None
        self.__button_memento_a1 = None
        self.__button_memento_a2 = None
        self.__button_e1 = None
        self.__button_e2 = None
        self.__button_memento_b1 = None
        self.__button_memento_b2 = None
        self.__button_memento_c1 = None
        self.__button_memento_c2 = None
        self.__button_memento_d1 = None
        self.__button_memento_d2 = None
        self.__button_memento_e1 = None
        self.__button_memento_e2 = None
        self.__button_memento_rs = None
        self.__button_rs = None
        self.__check_memento_a1 = None
        self.__check_memento_a2 = None
        self.__check_memento_b1 = None
        self.__check_memento_b2 = None
        self.__check_memento_c1 = None
        self.__check_memento_c2 = None
        self.__check_memento_d1 = None
        self.__button_memento_rs = None
        self.__check_memento_e2 = None
        self.__check_memento_d2 = None
        self.__check_memento_e1 = None

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №2')
        self.__controller = Controller()
        self.__set_functions_menu()
        self.__set_letter_buttons()
        self.__set_other_buttons()
        self.__set_answer_box()
        self.__set_const()
        self.__set_grid()

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

    def __set_const(self):
        # Братк
        self.__const_a1 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        self.__const_a2 = [[1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 1, 1, 1, 0]]
        # р
        self.__const_b1 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
        self.__const_b2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0]]
        # а
        self.__const_c1 = [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
        self.__const_c2 = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 1]]
        # т
        self.__const_d1 = [[1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
        self.__const_d2 = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]
        # к
        self.__const_e1 = [[1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]
        self.__const_e2 = [[1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 0], [1, 0, 1, 0, 0], [1, 0, 0, 1, 1]]

        self.__const_rs = [[1, 0, 0, 1, 1], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]

    def __set_letter_buttons(self):
        self.__button_frame = Frame(self.__window)

        self.__button_a1 = Button(self.__button_frame, text='А1', width=5, command=self.__set_const_a1)
        self.__button_a1.grid(column=0, row=0)
        self.__button_memento_a1 = Button(self.__button_frame, text='Запомнить А1',
                                          width=15, command=self.__read_letter_a1)
        self.__button_memento_a1.grid(column=1, row=0)
        self.__var_check_a1 = IntVar(0)
        self.__check_memento_a1 = Checkbutton(self.__button_frame, variable=self.__var_check_a1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a1.grid(column=2, row=0)

        self.__button_a2 = Button(self.__button_frame, text='А2', width=5, command=self.__set_const_a2)
        self.__button_a2.grid(column=0, row=1)
        self.__button_memento_a2 = Button(self.__button_frame, text='Запомнить А2',
                                          width=15, command=self.__read_letter_a2)
        self.__button_memento_a2.grid(column=1, row=1)
        self.__var_check_a2 = IntVar(0)
        self.__check_memento_a2 = Checkbutton(self.__button_frame, variable=self.__var_check_a2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a2.grid(column=2, row=1)

        self.__button_b1 = Button(self.__button_frame, text='B1', width=5, command=self.__set_const_b1)
        self.__button_b1.grid(column=0, row=2)
        self.__button_memento_b1 = Button(self.__button_frame, text='Запомнить B1',
                                          width=15, command=self.__read_letter_b1)
        self.__button_memento_b1.grid(column=1, row=2)
        self.__var_check_b1 = IntVar(0)
        self.__check_memento_b1 = Checkbutton(self.__button_frame, variable=self.__var_check_b1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b1.grid(column=2, row=2)

        self.__button_b2 = Button(self.__button_frame, text='B2', width=5, command=self.__set_const_b2)
        self.__button_b2.grid(column=0, row=3)
        self.__button_memento_b2 = Button(self.__button_frame, text='Запомнить B2',
                                          width=15, command=self.__read_letter_b2)
        self.__button_memento_b2.grid(column=1, row=3)
        self.__var_check_b2 = IntVar(0)
        self.__check_memento_b2 = Checkbutton(self.__button_frame, variable=self.__var_check_b2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b2.grid(column=2, row=3)

        self.__button_c1 = Button(self.__button_frame, text='C1', width=5, command=self.__set_const_c1)
        self.__button_c1.grid(column=0, row=4)
        self.__button_memento_c1 = Button(self.__button_frame, text='Запомнить C1',
                                          width=15, command=self.__read_letter_c1)
        self.__button_memento_c1.grid(column=1, row=4)
        self.__var_check_c1 = IntVar(0)
        self.__check_memento_c1 = Checkbutton(self.__button_frame, variable=self.__var_check_c1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_c1.grid(column=2, row=4)

        self.__button_c2 = Button(self.__button_frame, text='C2', width=5, command=self.__set_const_c2)
        self.__button_c2.grid(column=0, row=5)
        self.__button_memento_c2 = Button(self.__button_frame, text='Запомнить C2',
                                          width=15, command=self.__read_letter_c2)
        self.__button_memento_c2.grid(column=1, row=5)
        self.__var_check_c2 = IntVar(0)
        self.__check_memento_c2 = Checkbutton(self.__button_frame, variable=self.__var_check_c2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_c2.grid(column=2, row=5)

        self.__button_d1 = Button(self.__button_frame, text='D1', width=5, command=self.__set_const_d1)
        self.__button_d1.grid(column=0, row=6)
        self.__button_memento_d1 = Button(self.__button_frame, text='Запомнить D1',
                                          width=15, command=self.__read_letter_d1)
        self.__button_memento_d1.grid(column=1, row=6)
        self.__var_check_d1 = IntVar(0)
        self.__check_memento_d1 = Checkbutton(self.__button_frame, variable=self.__var_check_d1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_d1.grid(column=2, row=6)

        self.__button_d2 = Button(self.__button_frame, text='D2', width=5, command=self.__set_const_d2)
        self.__button_d2.grid(column=0, row=7)
        self.__button_memento_d2 = Button(self.__button_frame, text='Запомнить D2',
                                          width=15, command=self.__read_letter_d2)
        self.__button_memento_d2.grid(column=1, row=7)
        self.__var_check_d2 = IntVar(0)
        self.__check_memento_d2 = Checkbutton(self.__button_frame, variable=self.__var_check_d2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_d2.grid(column=2, row=7)

        self.__button_e1 = Button(self.__button_frame, text='E1', width=5, command=self.__set_const_e1)
        self.__button_e1.grid(column=0, row=8)
        self.__button_memento_e1 = Button(self.__button_frame, text='Запомнить E1',
                                          width=15, command=self.__read_letter_e1)
        self.__button_memento_e1.grid(column=1, row=8)
        self.__var_check_e1 = IntVar(0)
        self.__check_memento_e1 = Checkbutton(self.__button_frame, variable=self.__var_check_e1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_e1.grid(column=2, row=8)

        self.__button_e2 = Button(self.__button_frame, text='E2', width=5, command=self.__set_const_e2)
        self.__button_e2.grid(column=0, row=9)
        self.__button_memento_e2 = Button(self.__button_frame, text='Запомнить E2',
                                          width=15, command=self.__read_letter_e2)
        self.__button_memento_e2.grid(column=1, row=9)
        self.__var_check_e2 = IntVar(0)
        self.__check_memento_e2 = Checkbutton(self.__button_frame, variable=self.__var_check_e2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_e2.grid(column=2, row=9)

        self.__button_rs = Button(self.__button_frame, text='RS', width=5, command=self.__set_const_rs)
        self.__button_rs.grid(column=0, row=11)
        self.__button_memento_rs = Button(self.__button_frame, text='Запомнить RS',
                                          width=15, command=self.__read_letter_rs)
        self.__button_memento_rs.grid(column=1, row=11)
        self.__var_check_rs = IntVar(0)
        self.__check_memento_rs = Checkbutton(self.__button_frame, variable=self.__var_check_rs, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_rs.grid(column=2, row=11)

        self.__button_frame.place(x=405, y=0)

    def __set_other_buttons(self):
        self.__algorithm_frame = Frame(self.__window)
        self.__clean_button = Button(self.__algorithm_frame, text='Очистить поле', width=25, command=self.__clear)
        self.__clean_button.grid(column=0, row=0)
        self.__clean_all = Button(self.__algorithm_frame, text='Очистить всё', width=25, command=self.__clear_all)
        self.__clean_all.grid(column=0, row=1)
        self.__teach_button = Button(self.__algorithm_frame, text='Обучить', width=25, command=self.__teach_neuron)
        self.__teach_button.grid(column=0, row=2)
        self.__recognize_button = Button(self.__algorithm_frame, text='Распознать',
                                         width=25, command=self.__recognize)
        self.__recognize_button.grid(column=0, row=3)
        self.__algorithm_frame.place(x=405, y=320)

    def __recognize(self):
        if self.__controller.algorithm.letter_rs is None:
            print('\n>> Не введён rs')
        else:
            result = self.__controller.recognize()
            self.__set_result(result)

    def __read_letter_a1(self):
        print('\nWINDOW: символ A1 считан')
        self.__controller.read_letter_a1(self.__my_grid.titles)
        self.__var_check_a1.set(1)
        self.__const_a1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a1)

    def __set_const_a1(self):
        print('\nWINDOW: буква А1')
        self.__clear()
        self.__set_const_letter(self.__const_a1)

    def __read_letter_a2(self):
        print('\nWINDOW: символ A2 считан')
        self.__controller.read_letter_a2(self.__my_grid.titles)
        self.__var_check_a2.set(1)
        self.__const_a2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a2)

    def __set_const_a2(self):
        print('\nWINDOW: буква А2')
        self.__clear()
        self.__set_const_letter(self.__const_a2)

    def __read_letter_b1(self):
        print('\nWINDOW: символ B1 считан')
        self.__controller.read_letter_b1(self.__my_grid.titles)
        self.__var_check_b1.set(1)
        self.__const_b1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b1)

    def __set_const_b1(self):
        print('\nWINDOW: буква B1')
        self.__clear()
        self.__set_const_letter(self.__const_b1)

    def __read_letter_b2(self):
        print('\nWINDOW: символ B2 считан')
        self.__controller.read_letter_b2(self.__my_grid.titles)
        self.__var_check_b2.set(1)
        self.__const_b2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b2)

    def __set_const_b2(self):
        print('\nWINDOW: буква B2')
        self.__clear()
        self.__set_const_letter(self.__const_b2)

    def __read_letter_c1(self):
        print('\nWINDOW: символ C1 считан')
        self.__controller.read_letter_c1(self.__my_grid.titles)
        self.__var_check_c1.set(1)
        self.__const_c1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c1)

    def __set_const_c1(self):
        print('\nWINDOW: буква C1')
        self.__clear()
        self.__set_const_letter(self.__const_c1)

    def __read_letter_c2(self):
        print('\nWINDOW: символ C2 считан')
        self.__controller.read_letter_c2(self.__my_grid.titles)
        self.__var_check_c2.set(1)
        self.__const_c2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c2)

    def __set_const_c2(self):
        print('\nWINDOW: буква c2')
        self.__clear()
        self.__set_const_letter(self.__const_c2)

    def __read_letter_d1(self):
        print('\nWINDOW: символ D1 считан')
        self.__controller.read_letter_d1(self.__my_grid.titles)
        self.__var_check_d1.set(1)
        self.__const_d1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_d1)

    def __set_const_d1(self):
        print('\nWINDOW: буква D1')
        self.__clear()
        self.__set_const_letter(self.__const_d1)

    def __read_letter_d2(self):
        print('\nWINDOW: символ D2 считан')
        self.__controller.read_letter_d2(self.__my_grid.titles)
        self.__var_check_d2.set(1)
        self.__const_d2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_d2)

    def __set_const_d2(self):
        print('\nWINDOW: буква D2')
        self.__clear()
        self.__set_const_letter(self.__const_d2)

    def __read_letter_e1(self):
        print('\nWINDOW: символ E1 считан')
        self.__controller.read_letter_e1(self.__my_grid.titles)
        self.__var_check_e1.set(1)
        self.__const_e1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_e1)

    def __set_const_e1(self):
        print('\nWINDOW: буква E1')
        self.__clear()
        self.__set_const_letter(self.__const_e1)

    def __read_letter_e2(self):
        print('\nWINDOW: символ E2 считан')
        self.__controller.read_letter_e2(self.__my_grid.titles)
        self.__var_check_e2.set(1)
        self.__const_e2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_e2)

    def __set_const_e2(self):
        print('\nWINDOW: буква E2')
        self.__clear()
        self.__set_const_letter(self.__const_e2)

    def __read_letter_rs(self):
        print('\nWINDOW: символ RS считан')
        self.__controller.read_letter_rs(self.__my_grid.titles)
        self.__var_check_rs.set(1)
        self.__const_rs = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_rs)

    def __set_const_rs(self):
        print('\nWINDOW: буква RS')
        self.__clear()
        self.__set_const_letter(self.__const_rs)

    def __set_grid(self):
        self.__grid_frame = Frame(self.__window)
        self.__my_grid = MyGrid(5, 5, self.__grid_frame)
        self.__grid_frame.place(x=5, y=5)

    def __clear(self):
        print('\nWINDOW: Очищено поле рисования')
        self.__my_grid.titles = [[None for _ in range(self.__my_grid.count_cols)] for _ in
                                 range(self.__my_grid.count_rows)]
        self.__my_grid.grid.delete("all")

    def __clear_all(self):
        print('\nWINDOW: Очищено всё')
        self.__clear()
        self.__set_settings()

    def __set_const_letter(self, matrix):
        col, row = self.__my_grid.get_width_height()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    self.__my_grid.titles[i][j] \
                        = self.__my_grid.grid.create_rectangle(j * col, i * row, (j + 1) * col, (i + 1) * row,
                                                               fill="pink")
                else:
                    self.__my_grid.grid.delete(self.__my_grid.titles[i][j])
                    self.__my_grid.titles[i][j] = None

    def __set_answer_box(self):
        self.__answer_box_frame = Frame(self.__window)

        self.__a1_radiobutton = BooleanVar()
        self.__b1_radiobutton = BooleanVar()
        self.__c1_radiobutton = BooleanVar()
        self.__d1_radiobutton = BooleanVar()
        self.__e1_radiobutton = BooleanVar()
        self.__un_radiobutton = BooleanVar()
        self.__a1_radiobutton.set(0)
        self.__b1_radiobutton.set(0)
        self.__c1_radiobutton.set(0)
        self.__d1_radiobutton.set(0)
        self.__e1_radiobutton.set(0)
        self.__un_radiobutton.set(0)

        self.__result_label = Label(self.__answer_box_frame, text='Результат: ')
        self.__result_label.grid(column=1, row=0)

        self.__result_label.grid(column=1, row=1)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2',
                                           variable=self.__a1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_a.grid(column=2, row=1)

        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2',
                                           variable=self.__b1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_b.grid(column=3, row=1)

        self.__radiobutton_c = Radiobutton(self.__answer_box_frame, text='C1/C2',
                                           variable=self.__c1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_c.grid(column=4, row=1)

        self.__radiobutton_d = Radiobutton(self.__answer_box_frame, text='D1/D2',
                                           variable=self.__d1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_d.grid(column=5, row=1)

        self.__radiobutton_e = Radiobutton(self.__answer_box_frame, text='E1/E2',
                                           variable=self.__e1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_e.grid(column=6, row=1)

        self.__radiobutton_un = Radiobutton(self.__answer_box_frame, text='Неизвестно',
                                            variable=self.__un_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_un.grid(column=4, row=2)

        self.__answer_box_frame.place(x=5, y=400)

    def __set_functions_menu(self):
        self.__menu_frame = Frame(self.__window)
        self.__label_k_min = Label(self.__menu_frame, text='k =      0< ')
        self.__label_k_min.grid(column=0, row=0)
        self.__value_k = DoubleVar()
        self.__value_k.set(1.0)
        self.__entry_k = Entry(self.__menu_frame, textvariable=self.__value_k, width=15)
        self.__entry_k.grid(column=1, row=0)
        self.__label_k_min = Label(self.__menu_frame, text='<=1 ')
        self.__label_k_min.grid(column=2, row=0)
        self.__menu_frame.place(x=405, y=290)

    def __set_result(self, result):
        self.__a1_radiobutton.set(0)
        self.__b1_radiobutton.set(0)
        self.__c1_radiobutton.set(0)
        self.__d1_radiobutton.set(0)
        self.__e1_radiobutton.set(0)
        self.__un_radiobutton.set(0)
        if result[0] == 1:
            self.__a1_radiobutton.set(1)
            self.__b1_radiobutton.set(0)
            self.__c1_radiobutton.set(0)
            self.__d1_radiobutton.set(0)
            self.__e1_radiobutton.set(0)
            self.__un_radiobutton.set(0)
        elif result[1] == 1:
            self.__a1_radiobutton.set(0)
            self.__b1_radiobutton.set(1)
            self.__c1_radiobutton.set(0)
            self.__d1_radiobutton.set(0)
            self.__e1_radiobutton.set(0)
            self.__un_radiobutton.set(0)
        elif result[2] == 1:
            self.__a1_radiobutton.set(0)
            self.__b1_radiobutton.set(0)
            self.__c1_radiobutton.set(1)
            self.__d1_radiobutton.set(0)
            self.__e1_radiobutton.set(0)
            self.__un_radiobutton.set(0)
        elif result[3] == 1:
            self.__a1_radiobutton.set(0)
            self.__b1_radiobutton.set(0)
            self.__c1_radiobutton.set(0)
            self.__d1_radiobutton.set(1)
            self.__e1_radiobutton.set(0)
            self.__un_radiobutton.set(0)
        elif result[4] == 1:
            self.__a1_radiobutton.set(0)
            self.__b1_radiobutton.set(0)
            self.__c1_radiobutton.set(0)
            self.__d1_radiobutton.set(0)
            self.__e1_radiobutton.set(1)
            self.__un_radiobutton.set(0)
        else:
            self.__a1_radiobutton.set(0)
            self.__b1_radiobutton.set(0)
            self.__c1_radiobutton.set(0)
            self.__d1_radiobutton.set(0)
            self.__e1_radiobutton.set(0)
            self.__un_radiobutton.set(1)

    def __teach_neuron(self):
        if self.__controller.algorithm.letter_a1 is None:
            print('\nWINDOW: Символ A1 не введён')
        elif self.__controller.algorithm.letter_a2 is None:
            print('\nWINDOW: Символ A2 не введён')
        elif self.__controller.algorithm.letter_b1 is None:
            print('\nWINDOW: Символ B1 не введён')
        elif self.__controller.algorithm.letter_b2 is None:
            print('\nWINDOW: Символ B2 не введён')
        elif self.__controller.algorithm.letter_c1 is None:
            print('\nWINDOW: Символ C1 не введён')
        elif self.__controller.algorithm.letter_c2 is None:
            print('\nWINDOW: Символ C2 не введён')
        elif self.__controller.algorithm.letter_d1 is None:
            print('\nWINDOW: Символ D1 не введён')
        elif self.__controller.algorithm.letter_d2 is None:
            print('\nWINDOW: Символ D2 не введён')
        elif self.__controller.algorithm.letter_e1 is None:
            print('\nWINDOW: Символ E1 не введён')
        elif self.__controller.algorithm.letter_e2 is None:
            print('\nWINDOW: Символ E2 не введён')
        else:
            print('\n>> Вычисления при k = ', self.__value_k.get())
            self.__controller.teach_neuron(float(self.__value_k.get()))