var a = 3;
// make it bigger by 1
console.log(a + 1);


var b = 100;
// make it smaller by 7

console.log(b - 7);


var c = 44;
// double c's value
console.log(c * 2);


var d = 125;
// divide d's value by 5
console.log(d / 5);


var e = 8;
// what's the cube of e's value?
e = Math.pow(e, 3)
console.log(e);


var f1 = 123;
var f2 = 345;
// tell if f1 is bigger than f2 (as a boolean)
if (f1 > f2) {

    console.log(f1 + ' is bigger than ' + f2);

} else {

    console.log(f2 + ' is bigger than ' + f1);

}

var g1 = 350;
var g2 = 200;
// tell if the double of g2 is bigger than g1 (pras a boolean)
if (g2 * 2 > g1) {

    console.log(g2 + ' * 2 is bigger than ' + g1);

} else {

    console.log(g2 + '* 2 is not bigger than ' + g1);

}


var h = 1357988018575474;
// tell if h has 11 as a divisor (as a boolean)
if (h % 11 == 0) {

    console.log(11 + ' is divisior of ' + h );

} else {

    console.log(11 + ' is not divisior of ' + h );

}


var i1 = 10;
var i2 = 3;
// tell if i1 is higher than i2 squared and smaller than i2 cubed (as a boolean)
if (i1 > (i2*i2) && i1 < (i2*i2*i2)) {

    console.log(i1 + ' bigger than ' + i2 + ' cubed but smaller than ' + i2 + ' squared.');

}



var j = 1521;
// tell if j is dividable by 3 or 5 (as a boolean)
if (j % 3 == 0 || j % 5 == 0) {

    console.log(j + ' is dividable by 3 or 5');

}



var k = 'Apple';
// fill the k variable with its content 4 times
console.log(k);

var i = 0;

while (i < 2) {

    i++;
    k += k;

}

console.log(k);
