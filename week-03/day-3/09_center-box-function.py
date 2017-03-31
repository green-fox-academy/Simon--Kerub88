from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def square_drawn(size):
    size = size / 2
    square = canvas.create_rectangle(150 - size, 150 - size, 150 + size, 150 + size)

square_drawn(140)
square_drawn(100)
square_drawn(50)

root.mainloop()
