from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/exercises/drawing/purple-steps-3d/r4.png]

def square_maker(x, y):
    square = canvas.create_rectangle(x, x, y, y, fill = "purple")


for i in range(6):
    square_maker((1.7 ** i) * 5, 1.7 ** (i + 1) * 5)

root.mainloop()
