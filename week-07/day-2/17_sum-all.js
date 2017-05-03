'use strict';
// - Create a variable named `ai` with the following content: `[3, 4, 5, 6, 7]`
// - Log the sum of the elements in `ai` to the console

var ai = [3, 4, 5, 6, 7];

function sum1(listOfNumbers){
    var sum = 0;
    for (var i = 0; i < listOfNumbers.length; i++) {
        sum += listOfNumbers[i];
    }
    return sum
}

//////////////////////////////////////////////////////////////////////

function sum2(listOfNumbers){
    var sum = 0;
    listOfNumbers.forEach(function(num){
        sum += num
    })
    return sum
}

console.log(sum2(ai))
