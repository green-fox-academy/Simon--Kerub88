# Saturn is missing from the planetList
# Insert it into the correct position

planetList = ["Mercury","Venus","Earth","Mars","Jupiter","Uranus","Neptune"]


Planets_with_Saturn = []

for p in range(len(planetList)):
    if planetList[p] == "Jupiter":
        Planets_with_Saturn.append(planetList[p])
        Planets_with_Saturn.append("Saturn")
    else:
        Planets_with_Saturn.append(planetList[p])

for l in Planets_with_Saturn:
    print(l)


# print(Planets_with_Saturn)
