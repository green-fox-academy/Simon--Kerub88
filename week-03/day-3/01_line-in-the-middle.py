# create a 300x300 black canvas.
# draw a red horizontal line to its middle.
# draw a green vertical line to its middle.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = "300", height = "300")
canvas.pack()
black_line = canvas.create_line(0, 150, 300, 15, fill = "red")


mainloop()
