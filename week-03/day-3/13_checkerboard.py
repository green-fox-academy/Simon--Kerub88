from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

def chess_lines(x1, x2, y1, y2):
    square = canvas.create_rectangle(x1, x2, y1, y2)

for i in range(8):
    x1 = 0
    x2 = 0
    y1 = 37.5
    y2 = 37.5
    chess_lines(0, 0, 37.5, 37.5)
    x1 += i * 37.5
    y1 += i * 37.5

root.mainloop()
