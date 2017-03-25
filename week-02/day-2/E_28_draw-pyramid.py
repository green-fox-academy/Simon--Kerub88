# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#1234*
#123***
#  *****
# *******
#
# The pyramid should have as many lines as the number was




number = int(input("Type any number. HUMAN!: "))
x = 1

while (x <= number * 2):

    s = (number - (x // 2)) * " "
    print(s + "*" * x)
    x = x + 2
