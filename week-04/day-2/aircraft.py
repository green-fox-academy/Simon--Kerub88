class Carrier():

    def __init__(self, ammo = 2400):
        self.ammo = ammo
        self.health = 3000
        self.garage = []

    def add_aircraft(self, aircraft_name):
        self.garage.append(aircraft_name)

    def carrier_status()


    # def refill(self):
    #     self.ammo -= aircraft.max_ammo - aircraft.current_ammo
    #     aircraft.current_ammo += aircraft.max_ammo - aircraft.current_ammo
    #     return self.ammo, aircraft.current_ammo

class Aircraft(Carrier):

    def __init__(self, plane_type = "F16"):
        self.plane_type = plane_type
        if self.plane_type == "F16":
            self.max_ammo = 8
            self.current_ammo = 0
            self.base_damage = 30
        elif plane_type == "F35":
            self.max_ammo = 12
            self.current_ammo = 0
            self.base_damage = 50

    def refill(self, ammo_storage = 300):
        self.ammo_storage = ammo_storage
        self.ammo_storage -= self.max_ammo - self.current_ammo
        self.current_ammo += self.max_ammo - self.current_ammo
        return self.ammo_storage


    def fight(self):
        current_damage = self.current_ammo * self.base_damage
        self.current_ammo = 0
        return current_damage, self.current_ammo

    def get_status(self):
        print("Type: ", self.plane_type, ", Ammo: ", self.current_ammo, ", Base Damage: ", self.base_damage, ", All Damage: ", self.base_damage * self.current_ammo)


air1_F16 = Aircraft()
# air1_F16.get_status()
# air1_F16.refill()
# air1_F16.get_status()
# print(air1_F16.fight())
# air1_F16.get_status()


battlestar = Carrier()
battlestar.add_aircraft(air1_F16)
print(battlestar.garage)
