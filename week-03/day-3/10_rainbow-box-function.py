from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.



def square_drawn(size, color):
    size = size / 2
    square = canvas.create_rectangle(150 - size, 150 - size, 150 + size, 150 + size, fill = color)

color = ["red", "orange", "yellow", "green", "blue", "#4B0082", "#EE82EE"]
size = 300
for c in range(1, len(color)):
    square_drawn(size, color[c])
    size -= 20



square_drawn(140, "red")

root.mainloop()
