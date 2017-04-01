# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints:
#  - how many candies they have on average

students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

def candie_race(s_list):
    winners = ""
    for i in s_list:
        if i["candies"] > 4:
            winners += i["name"]
    return winners

print(candie_race(students))

def candie_count(s_list):
    candies = 0
    count = 0
    for i in s_list:
        candies += i["candies"]
        count += 1
    return candies / count

print(candie_count(students))
