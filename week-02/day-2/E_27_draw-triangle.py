# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

# number = int(input("Enter a long number. HUMAN!: "))
#
# for n in range(1, number + 1):
#
#     print("*"*n)


number = 5 

x = 1
while (x <= number):
    print("*" * x)
    x = x + 1
