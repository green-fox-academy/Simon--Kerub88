var lineCount = 7;



// Write a program that draws a
// diamond like this:
//
//
//    *
//   ***
//  *****
// *******
//  *****
//   ***
//    *
//
// The diamond should have as many lines as lineCount is

for (i = 0, numberOfSpaces = lineCount / 2,star = '*', space = ' ', collectionOfStars = 1; i < lineCount; i++) {

    if (lineCount / 2 > i) {

        console.log(space.repeat(numberOfSpaces) + star.repeat(collectionOfStars))
        
            if (collectionOfStars < 7) {
                collectionOfStars += 2
                numberOfSpaces -= 1
            }

    } else if (lineCount / 2 < i) {

        collectionOfStars -= 2
        numberOfSpaces += 1
        console.log(space.repeat(numberOfSpaces) + star.repeat(collectionOfStars))

    }


}
