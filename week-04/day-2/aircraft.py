class Aircraft():

    def fight(self):
        return self.current_ammo * self.base_damage

    def get_status(self):
        print("Type: ", self.type, ", Ammo: ", self.current_ammo, ", Base Damage: ", self.base_damage, ", All Damage: ", self.base_damage * self.current_ammo)


class F16(Aircraft):

    def __init__(self):
        self.type = "F16"
        self.max_ammo = 8
        self.current_ammo = 0
        self.base_damage = 30


class F35(Aircraft):

    def __init__(self):
        self.type = "F35"
        self.max_ammo = 12
        self.current_ammo = 0
        self.base_damage = 50


class Carrier():

    def __init__(self, ammo = 2400):
        self.ammo = ammo
        self.health = 3000
        self.garage = []

    def add_aircraft(self):
        pass

    def refill(self):
        self.ammo -= aircraft.max_ammo - aircraft.current_ammo
        aircraft.current_ammo += aircraft.max_ammo - aircraft.current_ammo
        return self.ammo, aircraft.current_ammo

airF35 = F35()
carrier1 = Carrier()
print(carrier1.ammo)
