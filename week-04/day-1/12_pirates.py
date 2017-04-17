# Pirates
#
# Create a Pirate class. While you can add other fields and methods, you must have these methods:-
#
# drink_some_rum() - intoxicates the Pirate some
# hows_it_going_mate() - when called, the Pirate replies, if drink_some_run was called:-
# 0 to 4 times, "Pour me anudder!"
# else, "Arghh, I'ma Pirate. How d'ya d'ink its goin?", the pirate passes out and sleeps it off.
# If you manage to get this far, then you can try to do the following.
#
# die() - this kills off the pirate, in which case, drinkSomeRum, etc. just result in he's dead.
# brawl(x) - where pirate fights another pirate (if that other pirate is alive) and there's a 1/3 chance, 1 dies, the other dies or they both pass out.
# And... if you get that far...
#
# Add a parrot.
#
# The Pirate Ship
#
# The place for the Pirates
#
# Create a Ship class.
# The Ship stores Pirate-s instances in a list as the crew and has one captain who is also a Pirate.
# When a ship is created it doesn't have a crew or a captain.
# The ship can be filled with pirates and a captain via fill_ship() method.
# Filling the ship with a captain and random number of pirates.
# Ships should be represented in a nice way on command line including information about
# captains consumed rum, state (passed out / died)
# number of alive pirates in the crew
# Ships should have a method to battle other ships: ship.battle(otherShip)
# should return true if the actual ship (this) wins
# the ship should win if its calculated score is higher
# calculate score: Number of Alive pirates in the crew - Number of consumed rum by the captain
# The loser crew has a random number of losses (deaths).
# The winner captain and crew has a party, including a random number of rum :)
# BattleApp
#
# Create a battle_app.py file
# Create 2 ships, fill them with pirates
# Have a battle!
# Armada
#
# Create an Armada class
# Contains Ship-s as a list
# Have a armada.war(otherArmada) method where two armada can engage in war
# it should work like merge sort
# first ship from the first armada battles the first of the other
# the loser gets skipped so the next ship comes in play from that armada
# whichever armada gets to the end of its ships loses the war
# return true if this is the winner
# WarApp
#
# Create a war_app.py file
# Create 2 armadas, fill them with ships
# Have a war!

# ////////////////////////////////////////////////////////////////////////////////////

# Code Design:
# Pirate class:
    # drink_some_rum() - intoxicates the Pirate some
    # hows_it_going_mate() - when called, the Pirate replies, if drink_some_rum was called:-
        # 0 to 4 times, "Pour me anudder!"
        # else, "Arghh, I'ma Pirate. How d'ya d'ink its goin?", the pirate passes out and sleeps it off.
    # die() - this kills off the pirate, in which case, drinkSomeRum, etc. just result in he's dead.
    # brawl(x) - where pirate fights another pirate (if that other pirate is alive) and there's a 1/3 chance, 1 dies, the other dies or they both pass out.
    # Add a parrot.

# ////////////////////////////////////////////////////////////////////////////////////


import random

class Pirate():

    def __init__(self, name = "Sea_Dog"):
        self.name = name
        self.rum_meter = 0
        self.alive = True
        self.captain = False

    def drink_some_rum(self, rum = 1):
        if self.alive == True:
            self.rum = rum
            self.rum_meter += rum
            return self.rum_meter
        else:
            print("He`s dead")

    def hows_it_going_mate(self):
        if self.alive == True:
            if self.rum_meter <= 4:
                return "Pour me anudder!"
            else:
                return "Arghh, I'ma Pirate. How d'ya d'ink its goin?"
        else:
            return "He`s dead"

    def die(self):
        self.alive = False

    def get_status(self):
        print("Captain status: " + str(self.captain) + ", Name: " + str(self.name) + ", who drunk " + str(self.rum_meter) + " rum and Alive Status is: " + str(self.alive))

    def brawl(self, pirate_a, pirate_b):
        if pirate_a.alive == True and pirate_b.alive == True:
            self.pirate_a = pirate_a
            self.pirate_b = pirate_b
            brawl_outcome = random.randrange(1, 4)
            if brawl_outcome == 1:
                pirate_a.die()
                return str(pirate_a.name) + " is dead, " + str(pirate_b.name) + " is the winner"
            if brawl_outcome == 2:
                pirate_b.die()
                return str(pirate_b.name) + " is dead, " + str(pirate_a.name) + " is the winner"
            else:
                return "They both passed out"
        else:
            return "Only alive pirates can brawl"

# The Pirate Ship
# The Ship stores Pirate-s instances in a list as the crew and has one captain who is also a Pirate.
# When a ship is created it doesn't have a crew or a captain.
# The ship can be filled with pirates and a captain via fill_ship() method.
# Filling the ship with a captain and random number of pirates.
# Ships should be represented in a nice way on command line including information about
# captains consumed rum, state (passed out / died)
# number of alive pirates in the crew
# Ships should have a method to battle other ships: ship.battle(otherShip)
# should return true if the actual ship (this) wins
# the ship should win if its calculated score is higher
# calculate score: Number of Alive pirates in the crew - Number of consumed rum by the captain
# The loser crew has a random number of losses (deaths).
# The winner captain and crew has a party, including a random number of rum :)

class Ship(Pirate):

    def __init__(self, ship_name):
        self.ship_name = ship_name
        self.crew_list = []
        self.available_captain = 0

    def fill_ship(self, captain_name):
        if self.available_captain == 0:
            self.ship_captain = Pirate(str(captain_name))
            self.ship_captain.captain = True
            self.crew_list.append(self.ship_captain)
            self.available_captain += 1
        number_of_pirates = random.randrange(5, 21)
        while number_of_pirates > 0:
            Sea_Dog = Pirate()
            self.crew_list.append(Sea_Dog)
            number_of_pirates -= 1

    def alive_crew_list(self):
        alive_pirate = 0
        for pirate in self.crew_list:
            if pirate.alive == True:
                alive_pirate += 1
        return alive_pirate

        # alive_pirate = 0
        # full_list = len(self.crew_list)
        # while full_list > 0:
        #     for pirate in self.crew_list:
        #         if pirate.alive == True:
        #             alive_pirate += 1
        #             full_list -= 1
        # return alive_pirate

    def getstatus(self):
        print("\n" +
        "*"*(11 + len(self.ship_name)), "\n"
        "Ship name: " + str(self.ship_name) + "\n" +
        "*"*(11 + len(self.ship_name)), "\n" +
        "Crew Members: " + str(self.alive_crew_list()) + "\n" +
        str(self.crew_list[0].get_status()))

    def battle(self, enemy_ship):
        self.enemy_ship = enemy_ship
        attacking_ship = self.alive_crew_list() - self.ship_captain.rum_meter
        defending_ship = enemy_ship.alive_crew_list() - enemy_ship.ship_captain.rum_meter
        if attacking_ship > defending_ship:
            crew_casualties = random.randrange(5, enemy_ship.alive_crew_list())
            while crew_casualties > 0:
                for pirates in enemy_ship.crew_list:
                    if pirates.alive:
                        pirates.alive = False
                        crew_casualties -= 1
                        break
            captain_party_rum = random.randrange(1, 3)
            self.ship_captain.drink_some_rum()
            return False
        elif attacking_ship < defending_ship:
            crew_casualties = random.randrange(5, self.alive_crew_list())
            while crew_casualties > 0:
                for pirates in self.crew_list:
                    if pirates.alive:
                        pirates.alive = False
                        crew_casualties -= 1
                        break
            captain_party_rum = random.randrange(1, 3)
            enemy_ship.ship_captain.drink_some_rum()
            return True


ship1 = Ship("Black Pearl")
ship1.fill_ship("Black Beard")
ship1.getstatus()
ship2 = Ship("Cursed Vagon")
ship2.fill_ship("Cursed Captain")
ship2.getstatus()
print(ship1.battle(ship2))
ship1.getstatus()
ship2.getstatus()
print(ship1.alive_crew_list())



# ship1.crew_list[3].drink_some_rum()
# ship1.crew_list[3].get_status()




# pirate1 = Pirate("Jack")
# print(pirate1.get_status())
# pirate1.drink_some_rum(2)
# print(pirate1.hows_it_going_mate())
# pirate1.drink_some_rum(3)
# print(pirate1.hows_it_going_mate())
# pirate2 = Pirate("Isaac")
# print(pirate1.brawl(pirate1, pirate2))
# print(pirate1.hows_it_going_mate())
