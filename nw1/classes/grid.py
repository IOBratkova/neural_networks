from tkinter import *


class MyGrid:
    def __init__(self, rows, cols, frame):
        self.frame = frame
        self.count_rows = rows
        self.count_cols = cols
        self.titles = [[None for _ in range(self.count_cols)] for _ in range(self.count_rows)]
        self.grid = Canvas(self.frame, width=300, height=300, borderwidth=5, background='white')
        self.grid.pack(anchor=NW)
        self.grid.bind("<Button-1>", self.call_back)
        self.col_width = None
        self.row_height = None

    def call_back(self, event):
        self.get_width_height()
        col = int(event.x // self.col_width)
        row = int(event.y // self.row_height)
        if not self.titles[row][col]:
            self.titles[row][col] = self.grid.create_rectangle(col * self.col_width, row * self.row_height, (col + 1) * self.col_width,
                                                 (row + 1) * self.row_height, fill="pink")
        else:
            self.grid.delete(self.titles[row][col])
            self.titles[row][col] = None

    def get_width_height(self):
        self.col_width = 300 / self.count_cols
        self.row_height = 300 / self.count_rows
        return self.col_width, self.row_height
