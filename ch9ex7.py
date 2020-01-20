# Exercise 9.7
# Creates an 8 by 8 grid with red vertical lines and blue horizontal lines
# Sawan Srivastava
# 1/18/2020
from tkinter import *
class LineGrid:
    def __init__(self):
        window = Tk()
        window.title("Line Grid")
        self.canvas = Canvas(window, width = 700, height = 600, bg = "white")
        self.canvas.pack()
        self.displayGrid()
    def displayGrid(self):
        x = 200
        y = 150
        for i in range(1,8):
            self.canvas.create_line(x, 100, x, 500, width = 1, fill = "red", tags = "line")
            x += 50
            i += 1
        for j in range(1,8):
            self.canvas.create_line(150, y, 550, y, width = 1, fill = "blue", tags = "line")
            y += 50
            j += 1
LineGrid()

