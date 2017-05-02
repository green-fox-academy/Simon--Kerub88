// Crate a program that draws a chess table like this
//
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %
// % % % %
//  % % % %

var lineWidth = 4
var drawStuff = '% '

for (var i = 1; i <= 8; i++) {

    if (i % 2 != 0) {
        console.log(drawStuff.repeat(lineWidth))
    }else if (i % 2 == 0) {
        console.log(' ' + drawStuff.repeat(lineWidth))
    }

}
