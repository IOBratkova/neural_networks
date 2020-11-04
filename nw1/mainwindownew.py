import copy
from tkinter import *

from classes.controllernew import Controller
from classes.grid import MyGrid
from classes.functions import ActivationFunctionConst


class MyWidger:
    def __init__(self):
        # Окно0
        self.__window = Tk()
        self.__window.wm_minsize(620, 470)
        self.__controller = None

        # Грида
        self.__grid_frame = None
        self.__my_grid = None

        # Кнопки
        self.__button_frame = None
        self.__button_memento_a1 = None
        self.__button_memento_a2 = None
        self.__button_memento_b1 = None
        self.__button_memento_b2 = None
        self.__button_memento_c1 = None
        self.__button_memento_c2 = None
        self.__button_memento_c3 = None
        self.__button_a1 = None
        self.__button_a2 = None
        self.__button_b1 = None
        self.__button_b2 = None
        self.__button_c1 = None
        self.__button_c2 = None
        self.__button_c3 = None

        # Заранее определенные буквы
        self.__const_a1 = None
        self.__const_a2 = None
        self.__const_b1 = None
        self.__const_b2 = None
        self.__const_c1 = None
        self.__const_c2 = None
        self.__const_c3 = None

        # Значения чекбоксов
        self.__var_check_a1 = None
        self.__var_check_a2 = None
        self.__var_check_b1 = None
        self.__var_check_b2 = None
        self.__var_check_c1 = None
        self.__var_check_c2 = None
        self.__var_check_c3 = None

        # Меню-функций
        self.__button_ok_function = None
        self.__menu_frame = None
        self.__var_options_menu = None
        self.__menu = None
        self.__label_k_min = None
        self.__value_k = None
        self.__entry_k = None
        self.__label_k_min = None

        # Алгоритм-фрейм
        self.__algorithm_frame = None
        self.__clean_button = None
        self.__clean_all = None
        self.__teach_button = None
        self.__recognize_button = None

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №1')
        self.__controller = Controller()
        self.__set_grid()
        self.__set_const()
        self.__set_letter_buttons()
        self.__set_functions_menu()
        self.__set_other_buttons()
        self.__set_answer_box()

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

    def __set_functions_menu(self):
        self.__menu_frame = Frame(self.__window)
        self.__function_label = Label(self.__menu_frame, text='Функция: ')
        self.__function_label.grid(column=0, row=0)

        self.__var_options_menu = StringVar(self.__menu_frame)
        func = ActivationFunctionConst()
        functions = [func.bipolar_function[0], func.binary_function[0]]
        self.__var_options_menu.set(functions[0])
        self.__menu = OptionMenu(self.__menu_frame, self.__var_options_menu, *functions)
        self.__menu.grid(column=1, row=0)

        # self.__button_ok_function = Button(self.__menu_frame, text='OK', width=1, command=self.__ok_button_click)
        # self.__button_ok_function.grid(column=2, row=0)

        self.__label_k_min = Label(self.__menu_frame, text='k =      0< ')
        self.__label_k_min.grid(column=0, row=0)
        self.__value_k = DoubleVar()
        self.__value_k.set(1.0)
        self.__entry_k = Entry(self.__menu_frame, textvariable=self.__value_k, width=15)
        self.__entry_k.grid(column=1, row=0)
        self.__label_k_min = Label(self.__menu_frame, text='<=1 ')
        self.__label_k_min.grid(column=2, row=0)
        self.__menu_frame.place(x=380, y=220)

    def __set_other_buttons(self):
        self.__algorithm_frame = Frame(self.__window)
        self.__clean_button = Button(self.__algorithm_frame, text='Очистить поле', width=25, command=self.__clear)
        self.__clean_button.grid(column=0, row=0)
        self.__clean_all = Button(self.__algorithm_frame, text='Очистить всё', width=25, command=self.__clear_all)
        self.__clean_all.grid(column=0, row=1)
        self.__teach_button = Button(self.__algorithm_frame, text='Обучить', width=25, command=self.__teach_neuron)
        self.__teach_button.grid(column=0, row=2)
        self.__recognize_button = Button(self.__algorithm_frame, text='Распознать', width=25, command=self.__recognize)
        self.__recognize_button.grid(column=0, row=3)
        self.__algorithm_frame.place(x=380, y=250)

    def __teach_neuron(self):
        if self.__controller.algorithm.letter_a1 is None:
            print('\nWINDOW: Символ A1 не введён')
        elif self.__controller.algorithm.letter_a2 is None:
            print('\nWINDOW: Символ A2 не введён')
        elif self.__controller.algorithm.letter_b1 is None:
            print('\nWINDOW: Символ B1 не введён')
        elif self.__controller.algorithm.letter_b2 is None:
            print('\nWINDOW: Символ B2 не введён')
        else:
            print('\n>> Вычисления при k = ', self.__value_k.get())
            self.__controller.teach_neuron(float(self.__value_k.get()))

    def __set_grid(self):
        self.__grid_frame = Frame(self.__window)
        self.__my_grid = MyGrid(5, 5, self.__grid_frame)
        self.__grid_frame.place(x=5, y=5)

    def __set_const(self):
        self.__const_a1 = [[1, 0, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 0, 0, 0, 1]]
        self.__const_a2 = [[1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
        self.__const_b1 = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
        self.__const_b2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        self.__const_c1 = [[1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
        self.__const_c2 = [[1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]
        self.__const_c3 = [[1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]

    def __set_letter_buttons(self):
        self.__button_frame = Frame(self.__window)

        self.__button_a1 = Button(self.__button_frame, text='А1', width=5, command=self.__set_const_a1)
        self.__button_a1.grid(column=0, row=0)
        self.__button_memento_a1 = Button(self.__button_frame, text='Запомнить А1', width=15,
                                          command=self.__read_letter_a1)
        self.__button_memento_a1.grid(column=1, row=0)
        self.__var_check_a1 = IntVar(0)
        self.__check_memento_a1 = Checkbutton(self.__button_frame, variable=self.__var_check_a1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a1.grid(column=2, row=0)

        self.__button_a2 = Button(self.__button_frame, text='А2', width=5, command=self.__set_const_a2)
        self.__button_a2.grid(column=0, row=1)
        self.__button_memento_a2 = Button(self.__button_frame, text='Запомнить А2', width=15,
                                          command=self.__read_letter_a2)
        self.__button_memento_a2.grid(column=1, row=1)
        self.__var_check_a2 = IntVar(0)
        self.__check_memento_a2 = Checkbutton(self.__button_frame, variable=self.__var_check_a2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a2.grid(column=2, row=1)

        self.__button_b1 = Button(self.__button_frame, text='B1', width=5, command=self.__set_const_b1)
        self.__button_b1.grid(column=0, row=2)
        self.__button_memento_b1 = Button(self.__button_frame, text='Запомнить B1', width=15,
                                          command=self.__read_letter_b1)
        self.__button_memento_b1.grid(column=1, row=2)
        self.__var_check_b1 = IntVar(0)
        self.__check_memento_b1 = Checkbutton(self.__button_frame, variable=self.__var_check_b1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b1.grid(column=2, row=2)

        self.__button_b2 = Button(self.__button_frame, text='B2', width=5, command=self.__set_const_b2)
        self.__button_b2.grid(column=0, row=3)
        self.__button_memento_b2 = Button(self.__button_frame, text='Запомнить B2', width=15,
                                          command=self.__read_letter_b2)
        self.__button_memento_b2.grid(column=1, row=3)
        self.__var_check_b2 = IntVar(0)
        self.__check_memento_b2 = Checkbutton(self.__button_frame, variable=self.__var_check_b2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b2.grid(column=2, row=3)

        self.__button_c1 = Button(self.__button_frame, text='C1', width=5, command=self.__set_const_c1)
        self.__button_c1.grid(column=0, row=4)
        self.__button_memento_c1 = Button(self.__button_frame, text='Запомнить C1', width=15,
                                          command=self.__read_letter_c1)
        self.__button_memento_c1.grid(column=1, row=4)
        self.__var_check_c1 = IntVar(0)
        self.__check_memento_c1 = Checkbutton(self.__button_frame, variable=self.__var_check_c1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_c1.grid(column=2, row=4)

        self.__button_c2 = Button(self.__button_frame, text='C2', width=5, command=self.__set_const_c2)
        self.__button_c2.grid(column=0, row=5)
        self.__button_memento_c2 = Button(self.__button_frame, text='Запомнить C2', width=15,
                                          command=self.__read_letter_c2)
        self.__button_memento_c2.grid(column=1, row=5)
        self.__var_check_c2 = IntVar(0)
        self.__check_memento_c2 = Checkbutton(self.__button_frame, variable=self.__var_check_c2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_c2.grid(column=2, row=5)

        self.__button_c3 = Button(self.__button_frame, text='C3', width=5, command=self.__set_const_c3)
        self.__button_c3.grid(column=0, row=6)
        self.__button_memento_c3 = Button(self.__button_frame, text='Запомнить C3', width=15,
                                          command=self.__read_letter_c3)
        self.__button_memento_c3.grid(column=1, row=6)
        self.__var_check_c3 = IntVar(0)
        self.__check_memento_c3 = Checkbutton(self.__button_frame, variable=self.__var_check_c3, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_c3.grid(column=2, row=6)

        self.__button_frame.place(x=380, y=0)

    def __read_letter_a1(self):
        print('\nWINDOW: A1 считан')
        self.__controller.read_letter_a1(self.__my_grid.titles)
        self.__var_check_a1.set(1)
        self.__const_a1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a1)

    def __set_const_a1(self):
        print('\nWINDOW: Константная буква А1 (И)')
        self.__clear()
        self.__set_const_letter(self.__const_a1)

    def __read_letter_a2(self):
        print('\nWINDOW: A2 считан')
        self.__controller.read_letter_a2(self.__my_grid.titles)
        self.__var_check_a2.set(1)
        self.__const_a2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a2)

    def __set_const_a2(self):
        print('\nWINDOW: Константная буква А2 (И)')
        self.__clear()
        self.__set_const_letter(self.__const_a2)

    def __read_letter_b1(self):
        print('\nWINDOW: B1 считан')
        self.__controller.read_letter_b1(self.__my_grid.titles)
        self.__var_check_b1.set(1)
        self.__const_b1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b1)

    def __set_const_b1(self):
        print('\nWINDOW: Константная буква B1')
        self.__clear()
        self.__set_const_letter(self.__const_b1)

    def __read_letter_b2(self):
        print('\nWINDOW: B2 считан')
        self.__controller.read_letter_b2(self.__my_grid.titles)
        self.__var_check_b2.set(1)
        self.__const_b2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b2)

    def __set_const_b2(self):
        print('\nWINDOW: Константная буква B2 (И)')
        self.__clear()
        self.__set_const_letter(self.__const_b2)

    def __read_letter_c1(self):
        print('\nWINDOW:> C1 считан')
        self.__controller.read_letter_c1(self.__my_grid.titles)
        self.__var_check_c1.set(1)
        self.__const_c1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c1)

    def __set_const_c1(self):
        print('\nWINDOW: Константная буква C1')
        self.__clear()
        self.__set_const_letter(self.__const_c1)

    def __read_letter_c2(self):
        print('\nWINDOW: C2 считан')
        self.__controller.read_letter_c2(self.__my_grid.titles)
        self.__var_check_c2.set(1)
        self.__const_c2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c2)

    def __set_const_c2(self):
        print('\nWINDOW: Константная буква C2')
        self.__clear()
        self.__set_const_letter(self.__const_c2)

    def __read_letter_c3(self):
        print('\nWINDOW: C3 считан')
        self.__controller.read_letter_c3(self.__my_grid.titles)
        self.__var_check_c3.set(1)
        self.__const_c3 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c3)

    def __set_const_c3(self):
        print('\nWINDOW: Константная буква C1')
        self.__clear()
        self.__set_const_letter(self.__const_c3)

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

    def __clear(self):
        print('\nWINDOW: Очищено поле рисования')
        self.__my_grid.titles = [[None for _ in range(self.__my_grid.count_cols)] for _ in
                                 range(self.__my_grid.count_rows)]
        self.__my_grid.grid.delete("all")

    def __clear_all(self):
        print('\nWINDOW: Очищено всё')
        self.__clear()
        self.__set_settings()

    def __recognize(self):
        if self.__controller.algorithm.letter_c1 is None and self.__controller.algorithm.letter_c2 is None and self.__controller.algorithm.letter_c3 is None:
            print('\n>> Не введён ни один символ C')
        else:
            result = self.__controller.recognize()
            self.__set_result(result)

    def __set_result(self, result):
        self.__a1_radiobutton.set(0)
        self.__b1_radiobutton.set(0)
        self.__a2_radiobutton.set(0)
        self.__b2_radiobutton.set(0)
        self.__a3_radiobutton.set(0)
        self.__b3_radiobutton.set(0)
        for r in result:
            if r[1] == 'C1':
                self.__set(r, self.__a1_radiobutton, self.__b1_radiobutton)
            if r[1] == 'C2':
                self.__set(r, self.__a2_radiobutton, self.__b2_radiobutton)
            if r[1] == 'C3':
                self.__set(r, self.__a3_radiobutton, self.__b3_radiobutton)

    def __set(self, r, button_a, button_b):
        if r[0][1] == 'A':
            button_a.set(1)
        else:
            button_b.set(1)

    def __set_answer_box(self):
        self.__answer_box_frame = Frame(self.__window)
        self.__a1_radiobutton = BooleanVar()
        self.__b1_radiobutton = BooleanVar()
        self.__a1_radiobutton.set(0)
        self.__b1_radiobutton.set(0)

        self.__a2_radiobutton = BooleanVar()
        self.__b2_radiobutton = BooleanVar()
        self.__a2_radiobutton.set(0)
        self.__b2_radiobutton.set(0)

        self.__a3_radiobutton = BooleanVar()
        self.__b3_radiobutton = BooleanVar()
        self.__a3_radiobutton.set(0)
        self.__b3_radiobutton.set(0)

        self.__result_label = Label(self.__answer_box_frame, text='Результат: ')
        self.__result_label.grid(column=1, row=0)

        self.__result_label = Label(self.__answer_box_frame, text='C1: ')
        self.__result_label.grid(column=1, row=1)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2',
                                           variable=self.__a1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_a.grid(column=2, row=1)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2',
                                           variable=self.__b1_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_b.grid(column=3, row=1)

        self.__result_label = Label(self.__answer_box_frame, text='C2: ')
        self.__result_label.grid(column=1, row=2)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2',
                                           variable=self.__a2_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_a.grid(column=2, row=2)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2',
                                           variable=self.__b2_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_b.grid(column=3, row=2)

        self.__result_label = Label(self.__answer_box_frame, text='C3: ')
        self.__result_label.grid(column=1, row=3)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2',
                                           variable=self.__a3_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_a.grid(column=2, row=3)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2',
                                           variable=self.__b3_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_b.grid(column=3, row=3)

        self.__answer_box_frame.place(x=5, y=370)
