# Aircraft Carrier
#
# Aircrafts
#
# Create a class that represents an aircraft
#
# There are 2 types of aircrafts: F16 and F35
#
# Both aircraft should track how many ammo it has
#
# F16
#
# Max ammo: 8
# Base damage: 30
# F35
#
# Max ammo: 12
# Base damage: 50
# All the aircrafts should be created with empty ammo store
#
# Methods:
#
# fight
#
# It should use all the ammos (set it to 0) and it should return the damage it took
# The damage is the multiplication of the base damage and the ammos
# refill
#
# It should take a number as parameter and substract as much ammo as possibe
# It can't have more ammo than the number or the max ammo
# It should return the remaining ammo
# Eg. Filling an empty F35 with 300 would completely fill the storage of the aircraft and would return the remaining 288
# get_type
#
# It should return it's type as a string
# get_status
#
# It should return a string like: Type F35, Ammo: 10, Base Damage: 50, All Damage: 500
# Carrier
#
# Create a class that represents an aircraft-carrier
#
# The carrier should be able to store aircrafts
# Each carrier should have a store of ammo represented as number
# The inital ammo should be give by a parameter in it's constructor
# It should store a health point as a number
# Methods:
#
# add_aircraft
#
# It should take a string as the type of the aircraft (F16 / F35) and add a new aircraft to its store
# fill
#
# It should fill all the aircraft with ammo and substract the needed ammo from the ammo storage
# If there is not enough ammo than it should start to fill the F35 types first
# If there is no ammo when this method is called it should throw an exception
# fight
#
# It should take another carrier as a refrence parameter and fire all the ammo from the aircrafts to it, than substract all the damage from it's health points
# get_status
#
# It should give back a string about it's and all of its aircrafts status like:
#
# Aircraft count: 4, Ammo Storage: 2300, Total damage: 2280
# Aircrafts:
# Type F35, Ammo: 12, Base Damage: 50, All Damage: 600
# Type F35, Ammo: 12, Base Damage: 50, All Damage: 600
# Type F35, Ammo: 12, Base Damage: 50, All Damage: 600
# Type F16, Ammo: 8, Base Damage: 30, All Damage: 240
# Type F16, Ammo: 8, Base Damage: 30, All Damage: 240
# If the health points are 0 than it should give back: It's dead Jim :(

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
            print("You can add exclusively F16 or F35")

    def refill(self, ammo_storage = 300):
        self.ammo_storage = ammo_storage
        self.ammo_storage -= self.max_ammo - self.current_ammo
        self.current_ammo += self.max_ammo - self.current_ammo
        return self.ammo_storage


    def fight(self):
        current_damage = self.current_ammo * self.base_damage
        self.current_ammo = 0
        return current_damage

    def get_status(self):
        print("Type: ", self.plane_type, ", Ammo: ", self.current_ammo, ", Base Damage: ", self.base_damage, ", All Damage: ", self.base_damage * self.current_ammo)

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
            damage += plane.fight()
        self.enemy.health = self.enemy.health - damage
        return self.enemy.health


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
print("\nEnemy carrier status:", battlestar.fight(cylon_baseship), "health \n")
print(battlestar.carrier_status())
