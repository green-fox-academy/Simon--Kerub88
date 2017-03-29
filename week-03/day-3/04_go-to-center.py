# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.s

from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def line_drawn(x, y):
    line = canvas.create_line(x, y, 150, 150)
    return line

line_drawn(50, 10)
line_drawn(300, 300)
line_drawn(0, 0)

root.mainloop()
