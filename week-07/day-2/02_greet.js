'use strict';
// - Create variable named `al` and assign the value `Greenfox` to it
// - Create a function called `greet` that greets it's input parameter
//     - Greeting is printing e.g. `Greetings, dear Greenfox`
//     - Prepare for the special case when no parameters are given
// - Greet `al`

var al = 'Greenfox';

function greet(subject) {

    if (typeof(subject) === 'string') {
    return 'Greeting, dear ' + subject

} else {

    return 'Please type a subject is a string form'

}

}

console.log(greet(al))
