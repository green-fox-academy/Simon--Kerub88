class Aircraft:

    def __init__(self, max_ammo = 8, current_ammo = 0, base_damage = 30):
        self.max_ammo = max_ammo
        self.current_ammo = current_ammo
        self.base_damage = base_damage

    def refill(self,):
        pass

    def fight(self):
        pass

    def get_status(self):
        print("Type: ", ", Ammo: ", self.current_ammo, ", Base Damage: ", self.base_damage, ", All Damage: ", self.base_damage * self.current_ammo)

air1 = Aircraft()
air1.get_status()
