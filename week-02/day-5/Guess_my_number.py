# Write a program where the program chooses a number between 1 and 100. The player is then asked to enter a guess. If the player guesses wrong, then the program gives feedback and ask to enter an other guess until the guess is correct.
#
# Make the range customizable (ask for it before starting the guessing).
# You can add lives. (optional)
# Example
#
# I've the number between 1-100. You have 5 lives.
#
# 20
# Too high. You have 4 lives left.
#
# 10
# Too low. You have 3 lives left.
#
# 15
# Congratulations. You won!
import random

print("\n"
"\n"
"\n"
"///////////////////////////////\n"
"\n"
      "Guess My Number! 0.1beta_build\n"
      "\n"
      "///////////////////////////////\n"
      "\n"
      "\n"
      "\n"
      "Set the range of guess\n"
      "Guess between: \n"
      "(first number?)" )


range1 = int(input())
print("(second number?)")
range2 = int(input())

my_number = random.randrange(range1, range2)

# print(my_number)

print("I thought a number between", range1, "-", range2)

tries = 3
found = False


if found:
    print("****************************\n"
    "\n"
    "YOU WON! That was the numbe I guessed\n"
    "\n"
    "****************************")

while (not found) and tries > 0:

    print("You have " + str(tries) + " tries. What is your guess?\n")
    guess = int(input())

    if guess < my_number:
        print("Not the number I guessed\n"
        "Try a higher number!\n")
        tries -= 1

    elif guess > my_number:
        print("Not the number I guessed\n"
        "Try a lower number\n")
        tries -= 1

    else:
        found = True
        print("**************************************\n"
        "\n"
        "YOU WON! That was the number I guessed\n"
         "\n"
        "**************************************")

if tries <= 0:
    print("****************************\n"
    "\n"
    "GAME OVER\n"
    "\n"
    "****************************\n"
    "\n"
    "My number was " + str(my_number) + "\n"
    "\n")
