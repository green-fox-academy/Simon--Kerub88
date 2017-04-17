from pirates import Pirate
from pirates import Ship


ship1 = Ship("Black Pearl")
ship1.fill_ship("Black Beard")
ship1.getstatus()
ship2 = Ship("Cursed Vagon")
ship2.fill_ship("Cursed Captain")
ship2.getstatus()
print(ship1.battle(ship2))
ship1.getstatus()
ship2.getstatus()
