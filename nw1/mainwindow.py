from tkinter import *
from classes.grid import MyGrid


class Widget:
    def __init__(self):
        self.__window = Tk()
        self.__window.wm_minsize(520, 300)
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

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №1')
        self.__set_grid()
        self.__set_pattern_buttons()
        self.__set_memento_buttons()
        self.__set_other_buttons()
        self.__set_answer_box()

    def __set_grid(self):
        self.__grid_frame = Frame(self.__window)
        self.__my_grid = MyGrid(5, 5, self.__grid_frame)
        self.__grid_frame.place(x=0, y=0)

    def __set_pattern_buttons(self):
        self.__pattern_frame = Frame(self.__window)
        self.__button_a1 = Button(self.__pattern_frame, text='А1', width=5)
        self.__button_a1.grid(column=0, row=0)
        self.__button_a2 = Button(self.__pattern_frame, text='А2', width=5)
        self.__button_a2.grid(column=0, row=1)
        self.__button_b1 = Button(self.__pattern_frame, text='B1', width=5)
        self.__button_b1.grid(column=0, row=2)
        self.__button_b2 = Button(self.__pattern_frame, text='B2', width=5)
        self.__button_b2.grid(column=0, row=3)
        self.__button_c = Button(self.__pattern_frame, text='C', width=5)
        self.__button_c.grid(column=0, row=6)
        self.__pattern_frame.place(x=275, y=2)

    def __set_memento_buttons(self):
        self.__memento_frame = Frame(self.__window)
        self.__button_memento_a1 = Button(self.__memento_frame, text='Запомнить А1', width=15)
        self.__button_memento_a1.grid(column=0, row=0)
        self.__check_memento_a1 = Checkbutton(self.__memento_frame, onvalue=1, offvalue=0, state=DISABLED)
        self.__check_memento_a1.grid(column=1, row=0)

        self.__button_memento_a2 = Button(self.__memento_frame, text='Запомнить А2', width=15)
        self.__button_memento_a2.grid(column=0, row=1)
        self.__check_memento_a2 = Checkbutton(self.__memento_frame, onvalue=1, offvalue=0, state=DISABLED)
        self.__check_memento_a2.grid(column=1, row=1)

        self.__button_memento_b1 = Button(self.__memento_frame, text='Запомнить B1', width=15)
        self.__button_memento_b1.grid(column=0, row=2)
        self.__check_memento_b1 = Checkbutton(self.__memento_frame, onvalue=1, offvalue=0, state=DISABLED)
        self.__check_memento_b1.grid(column=1, row=2)

        self.__button_memento_b2 = Button(self.__memento_frame, text='Запомнить B2', width=15)
        self.__button_memento_b2.grid(column=0, row=3)
        self.__check_memento_b2 = Checkbutton(self.__memento_frame, onvalue=1, offvalue=0, state=DISABLED)
        self.__check_memento_b2.grid(column=1, row=3)

        self.__button_memento_c = Button(self.__memento_frame, text='Запомнить C', width=15)
        self.__button_memento_c.grid(column=0, row=4)
        self.__check_memento_c = Checkbutton(self.__memento_frame, onvalue=1, offvalue=0, state=DISABLED)
        self.__check_memento_c.grid(column=1, row=4)

        self.__memento_frame.place(x=345, y=2)

    def __set_other_buttons(self):
        self.__algorithm_frame = Frame(self.__window)
        self.__clean_button = Button(self.__algorithm_frame, text='Очистить', width=25, command=self.__clear)
        self.__clean_button.grid(column=0, row=0)
        self.__teach_button = Button(self.__algorithm_frame, text='Обучить', width=25)
        self.__teach_button.grid(column=0, row=1)
        self.__recognize_button = Button(self.__algorithm_frame, text='Распознать', width=25)
        self.__recognize_button.grid(column=0, row=2)
        self.__algorithm_frame.place(x=275, y=160)

    def __set_answer_box(self):
        self.__answer_box_frame = Frame(self.__window)
        a_var = BooleanVar()
        a_var.set(0)
        b_var = BooleanVar()
        b_var.set(0)
        self.__result_label = Label(self.__answer_box_frame, text='Результат: ')
        self.__result_label.grid(column=0, row=0)
        self.__radiobutton_a = Radiobutton(self.__answer_box_frame, text='A1/A2', state=DISABLED, variable=a_var)
        self.__radiobutton_a.grid(column=1, row=0)
        self.__radiobutton_b = Radiobutton(self.__answer_box_frame, text='B1/B2', state=DISABLED, variable=b_var)
        self.__radiobutton_b.grid(column=2, row=0)
        self.__answer_box_frame.place(x=275, y=260)

    def __clear(self):
        self.__my_grid.titles = [[None for _ in range(self.__my_grid.count_cols)] for _ in
                                 range(self.__my_grid.count_rows)]
        self.__my_grid.grid.delete("all")
