'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs:
//  - how many candies they have on average

function candyCount(listOfStudents) {
    var candyKings = [];
    listOfStudents.forEach(function(student){
        if (student.candies > 4) {
            candyKings.push(student.name)
        }
    })
    return candyKings
}

console.log(candyCount(students))

function avgCandy(listOfStudents) {
    var candies = 0;
    var students = 0;
    listOfStudents.forEach(function(student) {
        candies += student.candies;
        students++;
    })
    return candies / students
}

console.log(avgCandy(students))
