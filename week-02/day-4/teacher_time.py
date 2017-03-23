number = 5
out = 0

for i in range(number + 1):
    out += i

print(out)

# //////////////////////////////////////

number = 5
out = 0

# szebb megoldas mert igy egytol szamol, nem nullatol
for i in range(1, number + 1):
    out += i

print(out)

# ///////////////////////////////////////

number = 5

def sum(n):
    out = 0
    for i in range(1, number + 1):
        out += i
        return out

print(out)

# ///////////////////////////////////////

# Ez azert nem jo mert a number kivul van a fugvenyen ezert egy feladatra lehet h
# jo, de kesobb nem tudom mas ertekkel ujrahasznalni a fuggvenyt, emrt nem ferek hozza
# a number megvaltoytatasahoz

number = 5

def sum(n):
    out = 0
    for i in range(1, number + 1):
        out += i
    return out

print(sum())

# ///////////////////////////////////////

number = 5

def sum(n):
    out = 0
    for i in range(1, number + 1):
        out += i
    return out

print(out)

# ///////////////////////////////////////
#
# Dictionary

pirate = {"name" : "Jack", "gold": 7, "has_wooden_lag": True}

print(pirate["pirate"])

# felulirasa egy erteknek vagy jellemzonek
pirate["gold"] = 8

# eggyes elemek lekerese
for key in pirate:
    print(key)
    print(pirate[key])

# masik modszer
for key, value in pirate.items():
    print(key)
    print(value])

for key in pirate:
    print(key + " : " + str(pirate[key]))

for key, value in pirate.items()
    print(key + " : ") + str(value))
