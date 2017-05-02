'use strict';
// - Write a function called `sum` that sum all the numbers until the given parameter
// - The function should return the result

function sum(number) {
    var sum = 0;
    if (typeof(number) === 'number') {

        for (var i = 0; i < number; i++) {

            sum += i;
        }

        return sum

    } else {

        return 'Add a number'

    }

}

console.log(sum(8))
