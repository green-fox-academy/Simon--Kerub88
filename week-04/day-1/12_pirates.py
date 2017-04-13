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

# The Pirate Ship

import random

class Pirate():

    def __init__(self, name):
        self.name = name
        self.rum_meter = 0
        self.alive = True

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



pirate1 = Pirate("Jack")
pirate1.drink_some_rum(2)
print(pirate1.hows_it_going_mate())
pirate1.drink_some_rum(3)
print(pirate1.hows_it_going_mate())
pirate2 = Pirate("Isaac")
print(pirate1.brawl(pirate1, pirate2))
print(pirate1.hows_it_going_mate())
