# An average Green Fox attendee codes 6 hours daily
# The semester is 17 weeks long
#
# Print how many hours is spent with coding in a semester by an attendee,
# if the attendee only codes on workdays.
#
# Print the percentage of the coding hours in the semester if the average
# work hours weekly is 52

print("An average Green Fox attendee codes " + str(6*17*5) + "h in the semester")


workHdays = 52
code_h_week = 6 * 5
print((code_h_week / workHdays) * (100))
