# Write a program that asks for two numbers
# Thw first number represents the number of girls that comes to a party, the
# second the boys
# It should print: The party is exellent!
# If the the number of girls and boys are equal and there are more people coming than 20
#
# It should print: Quite cool party!
# It there are more than 20 people coming but the girl - boy ratio is not 1-1
#
# It should print: Average party...
# If there are less people coming than 20
#
# It should print: Sausage party
# If no girls are coming, regardless the count of the people

print("Number of boys?")

boys = int(input())

print("And the girls?")

girls = int(input())

party_animals = boys + girls

if boys == girls and party_animals > 20:
    print("The party is exellent!")
elif boys != girls and party_animals > 20:
    print("Quite cool party!")
elif party_animals < 20 and girls >= 0:
    print("Average party...")
elif girls == 0 :
    print("Sausage party")











# Some old ideas, i will comeback for you! I promise. We left behind nooooooone!
# def party_indi():
#     if girls = boys:
#         print("The party of humans is mathematicaly exellent")
#     elif girls > boys or girls < boys:
#         print("The party of this humans is quiet cool!")
#
# party_indi(12,12)
