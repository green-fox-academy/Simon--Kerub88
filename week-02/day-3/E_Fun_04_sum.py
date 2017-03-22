# - Write a function called `sum` that sum all the numbers
#   until the given parameter


def sum(inpt_list):
    basic = 0
    for i in range(1, inpt_list+1):
        basic += i
    return basic

print(sum(3))
