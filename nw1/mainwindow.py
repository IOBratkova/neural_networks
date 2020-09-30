from tkinter import *
from classes.grid import MyGrid
from classes.functions import ActivationFunctionConst
from classes.controller import Controller


class Widget:
    def __init__(self):
        self.__window = Tk()
        # self.__controller = Controller()
        self.__window.wm_minsize(570, 350)
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
        self.__const_a1 = [[1, 0, 0, 0, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 0, 0, 0, 1]]
        self.__const_a2 = [[1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [1, 0, 1, 0, 1], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1]]
        self.__const_b1 = [[0, 1, 1, 1, 0], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [0, 1, 1, 1, 0]]
        self.__const_b2 = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]

    def __set_const_letter(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    self.__my_grid.titles[i][j] \
                        = self.__my_grid.grid.create_rectangle(j * self.__my_grid.col_width,
                                                               i * self.__my_grid.row_height,
                                                               (j + 1) * self.__my_grid.col_width,
                                                               (i + 1) * self.__my_grid.row_height,
                                                               fill="green")
                else:
                    self.__my_grid.grid.delete(self.__my_grid.titles[i][j])
                    self.__my_grid.titles[i][j] = None

    def __set_const_a1(self):
        print('>> Константная буква И1')
        self.__set_const_letter(self.__const_a1)

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №1')
        self.__controller = Controller()
        self.__set_grid()
        self.__set_pattern_buttons()
        self.__set_memento_buttons()
        self.__set_other_buttons()
        self.__set_answer_box()
        self.__set_functions_menu()

    def __set_grid(self):
        self.__grid_frame = Frame(self.__window)
        self.__my_grid = MyGrid(5, 5, self.__grid_frame)
        self.__grid_frame.place(x=0, y=0)

    def __set_functions_menu(self):
        self.__menu_frame = Frame(self.__window)
        self.__function_label = Label(self.__menu_frame, text='Функция: ')
        self.__function_label.grid(column=0, row=0)

        self.__var_options_menu = StringVar(self.__menu_frame)
        func = ActivationFunctionConst()
        functions = [func.binary_function[0], func.bipolar_function[0]]
        self.__var_options_menu.set(functions[0])
        self.__menu = OptionMenu(self.__menu_frame, self.__var_options_menu, *functions)
        self.__menu.grid(column=1, row=0)

        self.__button_ok = Button(self.__menu_frame, text='OK', width=1, command=self.__ok_button_click)
        self.__button_ok.grid(column=2, row=0)
        self.__menu_frame.place(x=325, y=0)

    def __ok_button_click(self):
        tmp = self.__var_options_menu.get()
        print('>> Выбрана ' + tmp + ' функция ')
        self.__controller.read_function(tmp)

    def __set_pattern_buttons(self):
        self.__pattern_frame = Frame(self.__window)
        self.__button_a1 = Button(self.__pattern_frame, text='А1', width=5, command=self.__set_const_a1)
        self.__button_a1.grid(column=0, row=0)
        self.__button_a2 = Button(self.__pattern_frame, text='А2', width=5)
        self.__button_a2.grid(column=0, row=1)
        self.__button_b1 = Button(self.__pattern_frame, text='B1', width=5)
        self.__button_b1.grid(column=0, row=2)
        self.__button_b2 = Button(self.__pattern_frame, text='B2', width=5)
        self.__button_b2.grid(column=0, row=3)
        self.__button_c = Button(self.__pattern_frame, text='C', width=5)
        self.__button_c.grid(column=0, row=6)
        self.__pattern_frame.place(x=325, y=40)

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

        self.__memento_frame.place(x=395, y=40)

    def __set_other_buttons(self):
        self.__algorithm_frame = Frame(self.__window)
        self.__clean_button = Button(self.__algorithm_frame, text='Очистить поле', width=25, command=self.__clear)
        self.__clean_button.grid(column=0, row=0)
        self.__clean_all = Button(self.__algorithm_frame, text='Очистить всё', width=25, command=self.__clear_all)
        self.__clean_all.grid(column=0, row=1)
        self.__teach_button = Button(self.__algorithm_frame, text='Обучить', width=25, command=self.__teach_neuron)
        self.__teach_button.grid(column=0, row=2)
        self.__recognize_button = Button(self.__algorithm_frame, text='Распознать', width=25)
        self.__recognize_button.grid(column=0, row=3)
        self.__algorithm_frame.place(x=325, y=200)

    def __set_answer_box(self):
        self.__answer_box_frame = Frame(self.__window)
        self.__a_radiobutton = BooleanVar()
        self.__a_radiobutton.set(0)
        self.__b_radiobutton = BooleanVar()
        self.__b_radiobutton.set(0)
        self.__result_label = Label(self.__answer_box_frame, text='Результат: ')
        self.__result_label.grid(column=1, row=0)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2', state=DISABLED,
                                           variable=self.__a_radiobutton)
        self.__radiobutton_a.grid(column=2, row=0)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2', state=DISABLED,
                                           variable=self.__b_radiobutton)
        self.__radiobutton_b.grid(column=3, row=0)
        self.__answer_box_frame.place(x=30, y=315)

    def __clear(self):
        print('>> Очищено поле рисования')
        self.__my_grid.titles = [[None for _ in range(self.__my_grid.count_cols)] for _ in
                                 range(self.__my_grid.count_rows)]
        self.__my_grid.grid.delete("all")

    def __clear_all(self):
        print('>> Очищено всё')
        self.__clear()
        self.__set_settings()

    def __read_letter_a1(self):
        print('>> A1 считан')
        self.__controller.read_letter_a1(self.__my_grid.titles)
        self.__var_check_a1.set(1)
        print(self.__controller.algorithm.letter_a1)

    def __read_letter_a2(self):
        print('>> A2 считан')
        self.__controller.read_letter_a2(self.__my_grid.titles)
        self.__var_check_a2.set(1)
        print(self.__controller.algorithm.letter_a2)

    def __read_letter_b1(self):
        print('>> В1 считан')
        self.__controller.read_letter_b1(self.__my_grid.titles)
        self.__var_check_b1.set(1)
        print(self.__controller.algorithm.letter_b1)

    def __read_letter_b2(self):
        print('>> В2 считан')
        self.__controller.read_letter_b2(self.__my_grid.titles)
        self.__var_check_b2.set(1)
        print(self.__controller.algorithm.letter_b2)

    def __read_letter_c(self):
        print('>> С считан')
        self.__controller.read_letter_c(self.__my_grid.titles)
        self.__var_check_c.set(1)
        print(self.__controller.algorithm.letter_c)

    def __teach_neuron(self):
        print('>> Обучение нейрона')
        self.__controller.teach_neuron()
