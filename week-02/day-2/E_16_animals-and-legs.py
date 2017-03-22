# Write a program that asks for two integers
# The first represents the number of chickens the farmer has
# The seconf represents the number of pigs the farmer has
# It should print how many legs all the animals have

print("Enter how many chickens do you have")
chickens = int(input())
print("Enter how many pigs do you have")
pigs = int(input())
legs = (chickens + pigs) * 4
print(legs, "legs your animals have")
