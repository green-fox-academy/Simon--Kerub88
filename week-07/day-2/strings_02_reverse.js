'use strict';
// Reverse the string!

var reversed = ".eslaf eb t'ndluow ecnetnes siht ,dehctiws erew eslaf dna eurt fo sgninaem eht fI"

function reverseStuff(str) {
    var splitString = reversed.split('');

    var reverseArray = splitString.reverse();

    var joinArray = reverseArray.join('');

    return joinArray;
}

reversed = reverseStuff(reversed);
console.log(reversed)


//////////////////////////////////////////////////
// Shorter version //
//////////////////////////////////////////////////

function reverseString(str) {
    return str.split("").reverse().join("");
}

reversed = reverseString(reversed);
console.log(reversed)
