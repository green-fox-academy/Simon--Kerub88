class Carrier():

    def __init__(self, ammo = 2400):
        self.ammo = ammo
        self.health = 3000
        self.garage = []

    def add_aircraft(self, aircraft_name):
        self.aircraft_name = aircraft_name
        if self.aircraft_name == "F16":
            F16 = Aircraft("F16")
            self.garage.append(F16)
        elif self.aircraft_name == "F35":
            F35 = Aircraft("F35")
            self.garage.append(F35)
        else:
            print("I take only F16 or F35")

    def fill(self):
        if self.ammo >= 0:
            for plane in self.garage:
                plane.current_ammo += plane.max_ammo - plane.current_ammo
                self.ammo -= plane.current_ammo
        else:
            return "The carrier is out of ammo"


    def carrier_status(self):
        damage = 0
        for plane in self.garage:
            damage += plane.current_ammo * plane.base_damage
        print("Aircraft count: ", str(len(self.garage)) + ", Ammor Storage: ", str(self.ammo) + ", Total damage: " + str(damage), "\n" + "Aircrafts:")
        for plane in self.garage:
            plane.get_status()



class Aircraft(Carrier):

    def __init__(self, plane_type):
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

battlestar = Carrier()
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F35")
battlestar.add_aircraft("F35")
battlestar.add_aircraft("F35")
print(battlestar.carrier_status())
battlestar.fill()
print(battlestar.carrier_status())



# air1_F16 = Aircraft()
# air1_F16.get_status()
# air1_F16.refill()
# air1_F16.get_status()
# print(air1_F16.fight())
# air1_F16.get_status()
