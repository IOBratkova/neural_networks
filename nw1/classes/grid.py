from tkinter import *


class MyGrid:
    def __init__(self, rows, cols, widget):
        self.widget = widget
        self.count_rows = rows
        self.count_cols = cols
        self.titles = [[None for _ in range(self.count_cols)] for _ in range(self.count_rows)]
        self.grid = Canvas(self.widget, width=250, height=250, borderwidth=5, background='white')
        self.grid.pack(anchor=NW)
        self.grid.bind("<Button-1>", self.call_back)

    def call_back(self, event):
        col_width = self.grid.winfo_width() / self.count_cols
        row_height = self.grid.winfo_height() / self.count_rows
        col = int(event.x // col_width)
        row = int(event.y // row_height)
        if not self.titles[row][col]:
            self.titles[row][col] = self.grid.create_rectangle(col * col_width, row * row_height, (col + 1) * col_width,
                                                 (row + 1) * row_height, fill="green")
        else:
            self.grid.delete(self.titles[row][col])
            self.titles[row][col] = None

