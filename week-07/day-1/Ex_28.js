var lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (i = lineCount, star = '*', collectionOfStars = 1, space = ' '; i > 0; i--, collectionOfStars += 2) {

    console.log(space.repeat(i) + star.repeat(collectionOfStars));
}
