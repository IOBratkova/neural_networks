from tkinter import *
from classes.grid import MyGrid
from classes.controllernew import Controller
import copy


class Widget:
    def __init__(self):
        self.__window = Tk()
        self.__window.wm_minsize(600, 400)
        self.__button_memento_a1 = None
        self.__button_memento_a2 = None
        self.__button_memento_b1 = None
        self.__button_memento_b2 = None
        self.__button_memento_c = None
        self.__button_a1 = None
        self.__button_a2 = None
        self.__button_b1 = None
        self.__button_b2 = None
        self.__button_c = None
        self.__clean_button = None
        self.__teach_button = None
        self.__recognize_button = None
        self.__radiobutton_a = None
        self.__radiobutton_b = None
        self.__result_label = None
        self.__const_a1 = None
        self.__const_a2 = None
        self.__const_b1 = None
        self.__const_b2 = None

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №4')
        self.__controller = Controller()
        self.__set_grid()
        self.__set_pattern_buttons()
        self.__set_memento_buttons()
        self.__set_other_buttons()
        self.__set_answer_box()
        # self.__set_functions_menu()
        self.__set_const()

    def __set_const_letter(self, matrix):
        col, row = self.__my_grid.get_width_height()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]:
                    self.__my_grid.titles[i][j] \
                        = self.__my_grid.grid.create_rectangle(j * col, i * row, (j + 1) * col, (i + 1) * row, fill="pink")
                else:
                    self.__my_grid.grid.delete(self.__my_grid.titles[i][j])
                    self.__my_grid.titles[i][j] = None

    def __read_letter_a1(self):
        print('\n>> A1 считан')
        self.__controller.read_letter_a1(self.__my_grid.titles)
        self.__var_check_a1.set(1)
        self.__const_a1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a1)

    def __read_letter_a2(self):
        print('\n>> A2 считан')
        self.__controller.read_letter_a2(self.__my_grid.titles)
        self.__var_check_a2.set(1)
        self.__const_a2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_a2)

    def __read_letter_b1(self):
        print('\n>> В1 считан')
        self.__controller.read_letter_b1(self.__my_grid.titles)
        self.__var_check_b1.set(1)
        self.__const_b1 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b1)

    def __read_letter_b2(self):
        print('\n>> В2 считан')
        self.__controller.read_letter_b2(self.__my_grid.titles)
        self.__var_check_b2.set(1)
        self.__const_b2 = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_b2)

    def __read_letter_c(self):
        print('\n>> С считан')
        self.__controller.read_letter_c(self.__my_grid.titles)
        self.__var_check_c.set(1)
        self.__const_c = copy.deepcopy(self.__my_grid.titles)
        print(self.__controller.algorithm.letter_c)

    def __set_const_a1(self):
        print('\n>> Константная буква А1 (И)')
        self.__clear()
        self.__set_const_letter(self.__const_a1)

    def __set_const_a2(self):
        print('\n>> Константная буква А2 (И)')
        self.__clear()
        self.__set_const_letter(self.__const_a2)

    def __set_const_b1(self):
        print('\n>> Константная буква B1 (O)')
        self.__clear()
        self.__set_const_letter(self.__const_b1)

    def __set_const_b2(self):
        print('\n>> Константная буква B2 (O)')
        self.__clear()
        self.__set_const_letter(self.__const_b2)

    def __set_const_c(self):
        print('\n>> Константная буква C')
        self.__clear()
        self.__set_const_letter(self.__const_c)

    def __set_const(self):
        self.__const_a1 = [[1, 0, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 0, 0, 0, 1]]
        self.__const_a2 = [[1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
        self.__const_b1 = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
        self.__const_b2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
        self.__const_c =  [[1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 1, 1, 1]]

    def __set_grid(self):
        self.__grid_frame = Frame(self.__window)
        self.__my_grid = MyGrid(5, 5, self.__grid_frame)
        self.__grid_frame.place(x=0, y=0)

    # def __set_functions_menu(self):
        # self.__menu_frame = Frame(self.__window)
        # self.__function_label = Label(self.__menu_frame, text='Функция: ')
        # self.__function_label.grid(column=0, row=0)
        #
        # self.__var_options_menu = StringVar(self.__menu_frame)
        # func = ActivationFunctionConst()
        # functions = [func.bipolar_function[0], func.binary_function[0]]
        # self.__var_options_menu.set(functions[0])
        # self.__menu = OptionMenu(self.__menu_frame, self.__var_options_menu, *functions)
        # self.__menu.grid(column=1, row=0)

        # self.__button_ok = Button(self.__menu_frame, text='OK', width=1, command=self.__ok_button_click)
        # self.__button_ok.grid(column=2, row=0)

        # self.__label_k_min = Label(self.__menu_frame, text='k =      0< ')
        # self.__label_k_min.grid(column=0, row=1)
        # self.__value_k = DoubleVar()
        # self.__value_k.set(1.0)
        # self.__entry_k = Entry(self.__menu_frame, textvariable=self.__value_k, width=5)
        # self.__entry_k.grid(column=1, row=1)
        # self.__label_k_min = Label(self.__menu_frame, text='<=1 ')
        # self.__label_k_min.grid(column=2, row=1)
        # self.__menu_frame.place(x=325, y=0)

    # def __ok_button_click(self):
    #     tmp = self.__var_options_menu.get()
    #     print('\n>> Выбрана ' + tmp + ' функция ')
    #     self.__controller.read_function(tmp)

    def __set_pattern_buttons(self):
        self.__pattern_frame = Frame(self.__window)
        self.__button_a1 = Button(self.__pattern_frame, text='А1', width=5, command=self.__set_const_a1)
        self.__button_a1.grid(column=0, row=0)
        self.__button_a2 = Button(self.__pattern_frame, text='А2', width=5, command=self.__set_const_a2)
        self.__button_a2.grid(column=0, row=1)
        self.__button_b1 = Button(self.__pattern_frame, text='B1', width=5, command=self.__set_const_b1)
        self.__button_b1.grid(column=0, row=2)
        self.__button_b2 = Button(self.__pattern_frame, text='B2', width=5, command=self.__set_const_b2)
        self.__button_b2.grid(column=0, row=3)
        self.__button_c = Button(self.__pattern_frame, text='C', width=5, command=self.__set_const_c)
        self.__button_c.grid(column=0, row=6)
        self.__pattern_frame.place(x=370, y=15)

    def __set_memento_buttons(self):
        self.__memento_frame = Frame(self.__window)

        self.__button_memento_a1 = Button(self.__memento_frame, text='Запомнить А1', width=15,
                                          command=self.__read_letter_a1)
        self.__button_memento_a1.grid(column=0, row=0)
        self.__var_check_a1 = IntVar(0)
        self.__check_memento_a1 = Checkbutton(self.__memento_frame, variable=self.__var_check_a1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a1.grid(column=1, row=0)

        self.__button_memento_a2 = Button(self.__memento_frame, text='Запомнить А2', width=15,
                                          command=self.__read_letter_a2)
        self.__button_memento_a2.grid(column=0, row=1)
        self.__var_check_a2 = IntVar(0)
        self.__check_memento_a2 = Checkbutton(self.__memento_frame, variable=self.__var_check_a2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_a2.grid(column=1, row=1)

        self.__button_memento_b1 = Button(self.__memento_frame, text='Запомнить B1', width=15,
                                          command=self.__read_letter_b1)
        self.__button_memento_b1.grid(column=0, row=2)
        self.__var_check_b1 = IntVar(0)
        self.__check_memento_b1 = Checkbutton(self.__memento_frame, variable=self.__var_check_b1, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b1.grid(column=1, row=2)

        self.__button_memento_b2 = Button(self.__memento_frame, text='Запомнить B2', width=15,
                                          command=self.__read_letter_b2)
        self.__button_memento_b2.grid(column=0, row=3)
        self.__var_check_b2 = IntVar(0)
        self.__check_memento_b2 = Checkbutton(self.__memento_frame, variable=self.__var_check_b2, onvalue=1, offvalue=0,
                                              state=DISABLED)
        self.__check_memento_b2.grid(column=1, row=3)

        self.__button_memento_c = Button(self.__memento_frame, text='Запомнить C', width=15,
                                         command=self.__read_letter_c)
        self.__button_memento_c.grid(column=0, row=4)
        self.__var_check_c = IntVar(0)
        self.__check_memento_c = Checkbutton(self.__memento_frame, variable=self.__var_check_c, onvalue=1, offvalue=0,
                                             state=DISABLED)
        self.__check_memento_c.grid(column=1, row=4)

        self.__memento_frame.place(x=420, y=15)

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
        self.__algorithm_frame.place(x=370, y=150)

    def __set_answer_box(self):
        self.__answer_box_frame = Frame(self.__window)
        self.__a_radiobutton = BooleanVar()
        self.__a_radiobutton.set(0)
        self.__b_radiobutton = BooleanVar()
        self.__b_radiobutton.set(0)
        self.__result_label = Label(self.__answer_box_frame, text='Результат: ')
        self.__result_label.grid(column=1, row=0)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2',
                                           variable=self.__a_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_a.grid(column=2, row=0)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2',
                                           variable=self.__b_radiobutton, value=1, state=DISABLED)
        self.__radiobutton_b.grid(column=3, row=0)
        self.__answer_box_frame.place(x=370, y=270)

    def __clear(self):
        print('\n>> Очищено поле рисования')
        self.__my_grid.titles = [[None for _ in range(self.__my_grid.count_cols)] for _ in
                                 range(self.__my_grid.count_rows)]
        self.__my_grid.grid.delete("all")

    def __clear_all(self):
        print('\n>> Очищено всё')
        self.__clear()
        self.__set_settings()

    def __teach_neuron(self):
        if self.__controller.algorithm.letter_a1 is None:
            print('\n>> Символ A1 не введён')
        elif self.__controller.algorithm.letter_a2 is None:
            print('\n>> Символ A2 не введён')
        elif self.__controller.algorithm.letter_b1 is None:
            print('\n>> Символ B1 не введён')
        elif self.__controller.algorithm.letter_b2 is None:
            print('\n>> Символ B2 не введён')
        else:
            pass
            # print('\n>> Вычисления при k = ', self.__value_k.get())
            # self.__controller.teach_neuron(float(self.__value_k.get()))

    def __recognize(self):
        if self.__controller.algorithm.letter_c is None:
            print('\n>> Символ C не введён')
        else:
            result = self.__controller.recognize()
            if result[1] == 'A':
                self.__a_radiobutton.set(1)
            else:
                self.__b_radiobutton.set(1)
