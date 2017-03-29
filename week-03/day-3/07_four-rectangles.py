from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
rec1 = canvas.create_rectangle (10, 15, 150, 55, fill = "green")
rec2 = canvas.create_rectangle (10, 60, 160, 155, fill = "blue")
rec3 = canvas.create_rectangle (100, 170, 145, 210, fill = "yellow")
rec4 = canvas.create_rectangle (200, 50, 300, 200, fill = "red")

root.mainloop()
