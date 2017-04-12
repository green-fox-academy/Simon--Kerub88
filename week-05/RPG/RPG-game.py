from tkinter import *

root = Tk()
height = 720
width = 720
canvas = Canvas(root, width = width, height = height)
canvas.pack()

# class Game():
#     def __init__(self):
        # root = Tk()
        # height = 720
        # width = 720
        # canvas = Canvas(root, width = width, height = height)
        # canvas.pack()
        # canvas.bind("<KeyPress>", on_key_press)

class Map():

    def __init__(self):
        self.draw_tiles()


    def draw_tiles(self):
        self.dungeon_map = [
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0,],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0,],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0,]
        ]

        self.floor_img = PhotoImage(file="floor.gif")
        self.wall_img = PhotoImage(file="wall.gif")

        for y in range(len(self.dungeon_map)):
            for x in range(len(self.dungeon_map[y])):
                if self.dungeon_map[y][x] == 0:
                    canvas.create_image(x * 72, y * 72, anchor = NW, image = self.floor_img)
                elif self.dungeon_map[y][x] == 1:
                    canvas.create_image(x * 72, y * 72, anchor = NW, image = self.wall_img)

        wall = self.dungeon_map[x][y] == 1

class Tiles(Map):

    def wall(self):
        self.wall_img = PhotoImage(file="wall.gif")
        canvas.create_image(x * 72, y * 72, anchor = NW, image = self.wall_img)

class Character():

    def __init__(self):
        self.tile_size = 72

dungeon = Map()

class Hero(Character):

    def __init__(self):
        super().__init__()
        self.hero_down = PhotoImage(file = 'hero-down.gif')
        self.hero_left = PhotoImage(file = 'hero-down.gif')
        self.hero_right = PhotoImage(file = 'hero-down.gif')
        self.hero_up = PhotoImage(file = 'hero-down.gif')
        self.hero = 0

    def drawn_hero(self, x = 0, y = 0):
        canvas.delete(self.hero)
        self.character_x = x
        self.character_y = y
        self.hero = canvas.create_image(self.character_x * self.tile_size, self.character_y * self.tile_size, image = self.hero_up, anchor = NW)

    def hero_move(self, x, y, direction):
        if 0 <= x <= 9 and 0 <= y <= 9:
            if dungeon.dungeon_map[y][x] == 0:
                canvas.delete(self.hero)
                self.character_y = y
                self.character_x = x
                self.hero = canvas.create_image(self.character_x * self.tile_size, self.character_y * self.tile_size, image = direction, anchor = NW)

hero = Hero()
hero.drawn_hero()

def on_key_press(e):
    if e.keycode == 8320768 or e.keycode == 852087:
        hero.hero_move(hero.character_x, hero.character_y - 1, hero.hero_up)

    elif e.keycode == 8255233 or e.keycode == 65651:
        hero.hero_move(hero.character_x, hero.character_y + 1, hero.hero_down)

    elif e.keycode == 8189699 or e.keycode == 131172:
        hero.hero_move(hero.character_x + 1, hero.character_y, hero.hero_right)

    elif e.keycode == 8124162 or e.keycode == 97:
        hero.hero_move(hero.character_x - 1, hero.character_y, hero.hero_left)


# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

root.mainloop()
