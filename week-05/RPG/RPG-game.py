from tkinter import *

class Map():

    def __init__(self, height, width):
        self.root = Tk()
        self.height = height
        self.width = width

        self.canvas = Canvas(self.root, width = self.width, height = self.height)
        self.canvas.pack()
        self.draw_tiles()
        self.root.mainloop()
        # Tell the canvas that we prepared a function that can deal with the key press events
        self.canvas.bind("<KeyPress>", on_key_press)
        # Select the canvas to be in focused so it actually recieves the key hittings
        self.canvas.focus_set()

    def draw_tiles(self):
        dungeon_map = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        ]

        self.floor_img = PhotoImage(file="floor.gif")
        self.wall_img = PhotoImage(file="wall.gif")

        for x in range(len(dungeon_map)):
            for y in range(len(dungeon_map[x])):
                if dungeon_map[x][y] == 0:
                    self.canvas.create_image(x * 72, y * 72, anchor = NW, image = self.floor_img)
                elif dungeon_map[cell][row] == 1:
                    self.canvas.create_image(x * 72, y * 72, anchor = NW, image = self.wall_img)


class Character():

    def __init__(self):
        pass


class Hero(Character):

    def __init__(self):
        self.character_x = 0
        self.character_y = 0
        self.hero_down = PhotoImage(file = 'hero-down.gif')
        self.hero.left = PhotoImage(file = 'hero-down.gif')
        self.hero.right = PhotoImage(file = 'hero-down.gif')
        self.hero.up = PhotoImage(file = 'hero-down.gif')

    def drawn_hero(self):
        self.hero = canvas.create_image(72 * self.character_x, 72 * self.character_y, image = self.hero_down, anchor = NW)




def on_key_press(e):
    if e.keycode == 8320768:
        if hero.character_y > 0:
            hero.character_y = hero.character_y - 72
        else:
            hero.character_y = hero.character_y


dungeon = Map(720, 720)
hero = Character()
hero.draw_hero()
