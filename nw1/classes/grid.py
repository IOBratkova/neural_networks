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
        self.col_width = self.grid.winfo_width() / self.count_cols
        self.row_height = self.grid.winfo_height() / self.count_rows

    def call_back(self, event):
        col_width = self.grid.winfo_width() / self.count_cols
        row_height = self.grid.winfo_height() / self.count_rows
        col = int(event.x // col_width)
        row = int(event.y // row_height)
        if not self.titles[row][col]:
            self.titles[row][col] = self.grid.create_rectangle(col * col_width, row * row_height, (col + 1) * col_width,
                                                 (row + 1) * row_height, fill="pink")
        else:
            self.grid.delete(self.titles[row][col])
            self.titles[row][col] = None

