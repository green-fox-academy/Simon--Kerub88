# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps/r3.png]
#
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

def square_maker(x, y):
    square = canvas.create_rectangle(x, x, y, y, fill = "purple")

x = 10
y = 20

for s in range(19):
    square_maker(x, y)
    x = y
    y += 10


root.mainloop()
