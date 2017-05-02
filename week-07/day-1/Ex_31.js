'use strict';
var lineCount = 6;


// Write a program that draws a
// square like this:
//
//
// %%%%%
// %%  %
// % % %
// %  %%
// %   %
// %%%%%
//
// The square should have as many lines as lineCount is

var emptySpace = ' ';
var draw = '%';

for (var i = 1; i <= lineCount; i++) {
    if (i === 1 || i === lineCount) {

        console.log(draw.repeat(lineCount));

    }else if (1 > i < lineCount) {

        console.log('%' + emptySpace.repeat(i - 2) + '%' + emptySpace.repeat(lineCount - i - 1) + '%');
        
    }

}
