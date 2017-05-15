// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
// Follow these steps:
//     Add a new test case
//     Instantiate your class
//     create a list of integers
//     use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
//     test your method with an empyt list
//     with a list with one element in it
//     with multiple elements in it
//     with a null
//     with a string
// Run them
// Fix your code if needed

let arrayOfNumbs = [2, 3, '6', 1];

function sumArrays(array){
    var sum = 0;
    for (var i = 0; i < array.length; i++) {
        if (typeof array[i] === 'number') {
            sum += array[i];
        } else {
            return 'One or more element of the array is not a number'
        }
    } return sum 

}
console.log(sumArrays(arrayOfNumbs));

//
//
// if (typeof element === 'number'){
//     sum += element;
// }else {
//     return 'One or more element of the array is not a number'
// }
// })
// return sum


module.exports = sumArrays;
