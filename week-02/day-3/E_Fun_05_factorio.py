# - Create a function called `factorio`
#   that returns it's input's factorial


# def factorio(numbers):
#     summa = 1
#     for n in range(1, numbers+1):
#         summa *= 1
#     return summa
#
# print(factorio(5))


def factorio(x):
    ossz = 1
    for i in range(1, x+1):
        ossz *= i
    return ossz

print(factorio(5))
