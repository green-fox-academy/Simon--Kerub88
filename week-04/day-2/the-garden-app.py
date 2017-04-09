class Garden:
    def __init__(self, water_amount = 4000):
        self.list_flowers = []
        self.list_tree = []
        self.water_amount = water_amount

    def add_tree(self, Tree):
        self.list_tree.append(Tree)

    def add_flower(self, Flower):
        self.list_flowers.append(Flower)

    def watering(self, amount = 40):
        self.amount = amount
        for element in self.list_tree:
            if element.current_water <= 10:
                element.current_water += (amount // plants_check()) * 0.4
        for element in self.list_flowers:
            if element.current_water <= 5:
                element.current_water += (amount // plants_check()) * 0.75

    def plants_check(self):
        dry_plants = 0
        for element in self.list_tree:
            if element.current_water <= 10:
                dry_plants += 1
        for element in self.list_flowers:
            if element.current_water <= 5:
                dry_plants += 1
        return dry_plants

    def report_status(self):
        






class Tree(Garden):
    def __init__(self, tree_type, max_water = 20, current_water = 0):
        self.max_water = max_water
        self.current_water = current_water
        self.tree_type = tree_type

class Flower(Garden):
    def __init__(self, flower_type, max_water = 10, current_water = 0):
        self.max_water = max_water
        self.current_water = current_water
        self.flower_type = flower_type


the_garden = Garden()
flower1 = Flower("blue")
flower2 = Flower("yellow")
tree1 = Tree("purple")
tree2 = Tree("orange")
the_garden.add_flower(flower1)
the_garden.add_flower(flower2)
the_garden.add_tree(tree1)
the_garden.add_tree(tree2)
the_garden.plants_check()
print()
