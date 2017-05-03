'use strict';
// - Create a variable named `aj`
//   with the following content: `[3, 4, 5, 6, 7]`
// - Reverse the order of the elements in `aj`
// 		- do it with the built in method
//		- do it with creating a new temp array and a loop
// - Print the elements of the reversed `aj`

var aj = [3, 4, 5, 6, 7];

console.log(aj.reverse());

/////////////////////////////////////////////////////////////////////

var aj2 = [3, 4, 5, 6, 7];
var tempAr = [];

for (var i = 0; i < aj2.length; i++) {
    tempAr.unshift(aj2[i]);
}

aj2 = tempAr

console.log(aj2)
