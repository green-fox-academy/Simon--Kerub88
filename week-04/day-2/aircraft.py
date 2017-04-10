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
            print("You can add exclusively F16 or F35 ")

    def fill(self):
        if self.ammo > 0:
            if self.ammo / len(self.garage) < 12:
                for plane in self.garage:
                    while plane.plane_type == "F35" and plane.current_ammo == 0:
                        if self.ammo > plane.max_ammo - plane.current_ammo:
                            self.ammo = plane.refill(self.ammo)
                        else:
                            return "\nThe carrier is out of ammo \n"
            if self.ammo / len(self.garage) > 0:
                for plane in self.garage:
                    if self.ammo > plane.max_ammo - plane.current_ammo:
                        self.ammo = plane.refill(self.ammo)
                    else:
                        return "\nThe carrier is out of ammo \n"
        else:
            return "\nThe carrier is out of ammo \n"


    def carrier_status(self):
        if self.health <= 0:
            print("It's dead Jim :(")
        else:
            damage = 0
            for plane in self.garage:
                damage += plane.current_ammo * plane.base_damage
            print("Aircraft count: ", str(len(self.garage)) + ", Ammo Storage: ", str(self.ammo) + ", Total damage: " + str(damage), "\n" + "Aircrafts:")
            for plane in self.garage:
                plane.get_status()

    def fight(self, enemy):
        self.enemy = enemy
        damage = 0
        for plane in self.garage:
            damage += plane.current_ammo * plane.base_damage
        self.enemy.health = self.enemy.health - damage
        return self.enemy.health


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
        else:
            print("You can add exclusively F16 or F35 ")

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

battlestar = Carrier(300)
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F16")
battlestar.add_aircraft("F35")
battlestar.add_aircraft("F35")
battlestar.add_aircraft("F35")
print(battlestar.carrier_status())
print(battlestar.fill())
print(battlestar.carrier_status())
cylon_baseship = Carrier(300)
print(battlestar.fight(cylon_baseship))
