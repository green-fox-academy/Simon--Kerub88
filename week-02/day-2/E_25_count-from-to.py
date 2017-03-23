# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
#
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

print("Gimme a number, HUMAN!")
n1 = int(input())
print("Goooood, GOOOOOOD. Now gimme a number again!")
n2 = int(input())

if n2 < n1:
    print("The second number should be bigger")
elif n2 > n1:
    for n in range(n1, n2):
        print (n)
