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

    # def on_key_press(self, e):
    #     if e.keycode == 8320768 or e.keycode == 852087:
    #         if hero.character_y > 0:
    #             hero.character_y = hero.character_y - 72
    #         else:
    #             hero.character_y = hero.character_y
    #
    #     elif e.keycode == 8255233:
    #         if hero.character_y < 720:
    #             hero.character_y = hero.character_y + 72
    #         else:
    #             hero.character_y = hero.character_y

class Map():

    def __init__(self):
        # self.root = Tk()
        # self.height = height
        # self.width = width

        # self.canvas = Canvas(self.root, width = self.width, height = self.height)
        # self.canvas.pack()
        self.draw_tiles()
        # # Tell the canvas that we prepared a function that can deal with the key press events
        # self.canvas.bind("<KeyPress>", on_key_press)
        # # Select the canvas to be in focused so it actually recieves the key hittings
        # self.canvas.focus_set()
        # self.root.mainloop()

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
                    canvas.create_image(x * 72, y * 72, anchor = NW, image = self.floor_img)
                elif dungeon_map[cell][row] == 1:
                    canvas.create_image(x * 72, y * 72, anchor = NW, image = self.wall_img)


class Character():

    def __init__(self):
        self.tile_size = 72

dungeon = Map()

class Hero(Character):

    def __init__(self):
        super().__init__()
        # self.character_x = 1
        # self.character_y = 1
        self.hero_down = PhotoImage(file = 'hero-down.gif')
        self.hero_left = PhotoImage(file = 'hero-down.gif')
        self.hero_right = PhotoImage(file = 'hero-down.gif')
        self.hero_up = PhotoImage(file = 'hero-down.gif')
        self.hero = 0

    def drawn_hero(self, x = 0, y = 0):
        canvas.delete(self.hero)
        self.character_x = x
        self.character_y = y
        self.hero = canvas.create_image(self.character_x * self.tile_size, self.character_y * self.tile_size, image = self.hero_down, anchor = NW)

hero = Hero()
hero.drawn_hero()

def on_key_press(e):
    if e.keycode == 8320768 or e.keycode == 852087:
        if hero.character_y >= 0:
            hero.character_y = hero.character_y - 1
            hero.drawn_hero(hero.character_x, hero.character_y)
        else:
            hero.character_y = hero.character_y

    elif e.keycode == 8255233:
        if hero.character_y < 720:
            hero.character_y = hero.character_y + 1
            hero.drawn_hero(hero.character_x, hero.character_y)
        else:
            hero.character_y = hero.character_y
    # elif e.keycode == 8255233:
    #     hero.character_y = hero.character_y + 1
    #     hero.drawn_hero(hero.character_x, hero.character_y)
    #
    # elif e.keycode == 8255233:
    #     hero.character_y = hero.character_y + 1
    #     hero.drawn_hero(hero.character_x, hero.character_y)


# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

root.mainloop()
