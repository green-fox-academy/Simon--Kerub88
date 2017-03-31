from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width='600', height='560')
canvas.pack()

def draw_polygon(x, y, size, x2, y2, size2):
    canvas.create_polygon(x, y, size, y, size / 2, size, fill = "#cc9933", outline = "black", width=2)

def recursive_polygons(x, y, size, x2, y2, size2):
    draw_polygon(x, y, size, x2, y2, size2)
    time.sleep(0.4)
    canvas.update()
    if size > 10:
        recursive_polygons(x, y, x + size/2, y, x + size/4, y + size/2)
        recursive_polygons(x + size / 2, y, x + size, y, x + size * 3/4, y + size / 2)
        recursive_polygons(x + size / 4, y + size / 2, x + size * 3/4, y + size / 2, x + size / 2, y + size)


recursive_polygons(20, 10, 560, 0, 0, 0)

root.mainloop()
