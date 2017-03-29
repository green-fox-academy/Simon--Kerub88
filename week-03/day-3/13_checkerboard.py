# fill the canvas with a checkerboard pattern.

from tkinter import *

def grid_maker(canvas, line_distance):
    for x in range(line_distance,canvas_width,line_distance):
       canvas.create_line(x, 0, x, canvas_height, fill="#476042")
    for y in range(line_distance,canvas_height,line_distance):
       canvas.create_line(0, y, canvas_width, y, fill="#476042")

root = Tk()
canvas_width = 300
canvas_height = 300
w = Canvas(root,
            width = canvas_width,
            height = canvas_height)
w.pack()

grid_maker(w, 37.5)

# canvas = Canvas(root, width='300', height='300')
# canvas.pack()










# def chess_lines(x1, y2, cell_size):
#     square = canvas.create_rectangle(x1, x2, y1, y2)
#
# x1 = 0
# x2 = 0
# y1 = 37.5
# y2 = 37.5
#
# for i in range(8):
#
#     chess_lines(x1, x2, y1, y2)
#     x1 += i * 37.5
#     y1 += i * 37.5
#     y2 += i * 37.5

root.mainloop()
