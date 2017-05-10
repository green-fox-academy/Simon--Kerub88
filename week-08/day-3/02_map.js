'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

let letterSelector = fruits.map(function(i){
    let splitListofLetters = i.split('');
    let splitedList = splitListofLetters.filter(function(x){
        return x === 'e'
    })
    return splitedList.length
})

console.log(letterSelector);

// sofisticated solution

let letter = fruits.map(function(x){
    return x.split('e').length - 1;
})
