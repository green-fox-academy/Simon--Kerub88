'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(num) {
    var factorial = 1;
    if (typeof(num) === 'number') {

        for (var i = 1; i <= num; i++) {

            factorial *= i;

        }

        return factorial

    } else {

        return 'Add a number'

    }

}

console.log(factorio(5))
