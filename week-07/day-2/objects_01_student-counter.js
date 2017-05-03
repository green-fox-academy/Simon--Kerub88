'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs:
// - how many candies are owned by students
//
// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function candyCounter(listOfStudents) {
    var candies = 0
    for (var i = 0; listOfStudents.length > i; i++){
        candies += listOfStudents[i].candies
    }
    return candies
}

console.log(candyCounter(students))

function studentsAge(listOfStudents) {
    var age = 0;

    listOfStudents.forEach(function(student) {
        if (student.candies < 5) {
            age += student.age;
        }
    })
    return age
}

console.log(studentsAge(students))
