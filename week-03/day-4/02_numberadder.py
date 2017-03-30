# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def add_number(number):
    if number == 1:
        return 1
    else:
        return number + add_number(number-1)

print(add_number(7))
