# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

number = str(input("Enter a number. HUMAN!: "))

num_list = list(number + "1")

for n in range(0, len(num_list)):
    num_list[n] = n * "*"

    print(num_list[n])
