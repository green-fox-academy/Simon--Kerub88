current_hours = 14;
current_minutes = 34;
current_seconds = 42;

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables

TotalDaySeconds = 60*60*24
print(TotalDaySeconds)
current_seconds = (14*60*60) + (34*60) + 42
print(current_seconds)
print("Remaining seconds from the Day: " + str(TotalDaySeconds - current_seconds))
