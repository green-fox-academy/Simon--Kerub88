from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='560')
canvas.pack()

def draw_polygon(x, y, size):
    canvas.create_polygon(x, y, x+size, y, size / 2, size, fill = "white", outline = "black", width=2)

def recursive_polygons(x, y, size):
    draw_polygon(x, y, size)
    time.sleep(0.04)
    canvas.update()
    if size > 10:
        recursive_polygons(x, y, size/2)
        recursive_polygons(x + size / 2, y, size/2)
        recursive_polygons(x + size / 4, y+ size / 2, size/2)


recursive_polygons(20, 10, 560)

root.mainloop()
