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
      "Guess between: (first number?)" )


range1 = int(input())
print("second number?")
range2 = int(input())

print("I thought a number between", range1, "-", range2)
