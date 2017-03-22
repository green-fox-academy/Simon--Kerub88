# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

print("Enter how many cigs do you smoke on monday?")
monday = int(input())
print("Enter how many cigs do you smoke on tuesday?")
tuesday = int(input())
print("Enter how many cigs do you smoke on wednesday?")
wednesday = int(input())
print("Enter how many cigs do you smoke on thursday?")
thursday = int(input())
print("Enter how many cigs do you smoke on friday?")
friday = int(input())

summary = monday + tuesday + wednesday + thursday + friday
avarage = summary / 5

print("Sum:", summary, "Avg:", avarage)
