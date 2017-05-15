'use strict';
// Write a function, that takes a string as an argument and returns a dictionary with all letters in the string as keys, and numbers as values that shows how many occurrences there are.
// Create a test for that.

let countLetters = function(string){
    let splitString = string.split('')
    let stringDictionary = {};
    for (var i = 0; i < splitString.length; i++) {
        let keyS = splitString[i];
        if (splitString[i] in stringDictionary) {
            stringDictionary[splitString[i]] += 1;
        } else {
            stringDictionary[splitString[i]] = 1;
    }
    }
    return stringDictionary
}

console.log(countLetters('summer'));
