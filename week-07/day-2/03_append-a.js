'use strict';
// - Create a variable named `am` and assign the value `kuty` to it
// - Write a function called `appendA` that gets a string as an input
//   and appends an 'a' character to its end
// - Print the result of `appendA(am)` to the console

var am = 'kuty';

function appendA(word) {

    if (typeof(word) === 'string') {

        return word + 'a'

    } else {

        return 'Type a word in string form'

    }

}

console.log(appendA(am))
