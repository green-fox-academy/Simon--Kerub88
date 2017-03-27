# - Create a function called `factorio`
#   that returns it's input's factorial


def factorio(numbers):
    summa = 1
    for n in range(1, numbers+1):
        summa *= n
    return summa

print(factorio(5))
