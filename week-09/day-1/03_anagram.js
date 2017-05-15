// Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
// Create a test for that.
'use strict';


let anagram = function(string1, string2) {
    if (string1.toLowerCase().split('').sort().join() === string2.toLowerCase().split('').sort().join()) {
        return true
    } else {
        return false
    }
}

module.exports = anagram;

console.log(anagram('kaloz', 'zolak'));
