from tkinter import *
from classes.grid import MyGrid


class Widget:
    def __init__(self):
        self.__window = Tk()
        self.__window.wm_minsize(640, 480)
        self.__my_grid = MyGrid(5, 5, self.__window)

    def __set_settings(self):
        self.__window.title('Нейронные сети, лабораторная работа №1')
        self.__my_grid.set_gird()

    def start(self):
        self.__set_settings()
        self.__window.mainloop()

