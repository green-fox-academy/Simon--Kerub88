from tkinter import *

class Map():

    def __init__(self, width, height):
        self.root = Tk()
        self.width = width
        self.height = height
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.canvas.bind("<KeyPress>", on_key_press)

        self.draw_tiles()
        self.root.mainloop()

    def draw_tiles(self):
        map = [
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
        self.floor_img = PhotoImage(file="floor.gif")
        self.wall_img = PhotoImage(file="wall.gif")
        for row in range(len(map)):
            for cell in range(len(map[row])):
                if map[cell][row] == 0:
                    self.canvas.create_image(row*72, cell*72, anchor=NW, image=self.floor_img)
                else:
                    self.canvas.create_image(row*72, cell*72, anchor=NW, image=self.wall_img)

    def on_key_press(e):
        if e.keycode == 8320768:
            if box.testBoxY > 0:
                box.testBoxY = box.testBoxY - 74
            else:
                box.testBoxY = box.testBoxY

        elif e.keycode == 8255233:
            if box.testBoxY < 720:
                box.testBoxY = box.testBoxY + 74
            else:
                box.testBoxY = box.testBoxY


        elif e.keycode == 8189699:
            if box.testBoxX < 720:
                box.testBoxX = box.testBoxX + 74
            else:
                box.testBoxX = box.testBoxX


        elif e.keycode == 8124162:
            if box.testBoxX > 0:
                box.testBoxX = box.testBoxX - 74
            else:
                box.testBoxX = box.testBoxX


game = Map(720, 720)
