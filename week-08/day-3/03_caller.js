'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber(array, callback) {
    let newList = array.filter(function(value) {
        return value % 2 == 0;
    })
    callback(newList.pop())
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8

// function lastEvenNumb(value){
//     return value % 2 == 0;
// }
//
// var listaaa = [2, 5, 7, 8, 9, 11];
// var newlistaaa = listaaa.filter(lastEvenNumb);
//
// console.log(newlistaaa.pop());
