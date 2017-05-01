var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

var oneDay = 24*60*60;

console.log(oneDay);
console.log('The remaining seconds from the day: ' + (oneDay - ((currentHours * 60 * 60) + (currentMinutes * 60) + 42)));
