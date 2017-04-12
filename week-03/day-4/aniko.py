from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='600')
canvas.pack()

def draw_square(x, y, size):
    canvas.create_oval(x, y, x+size, y+size, outline="green", width=2)

def recursive_something(x, y, size):
    draw_square(x, y, size)
    time.sleep(0.1)
    canvas.update()
    if size > 20:
        recursive_something(x, y, size/3)
        recursive_something(x+2/3*size, y, size/3)
        recursive_something(x, y+2/3*size, size/3)
        recursive_something(x+2/3*size, y+2/3*size, size/3)

recursive_something(10, 10, 500)

root.mainloop()
