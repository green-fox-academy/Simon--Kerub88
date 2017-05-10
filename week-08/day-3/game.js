'use strict';
// Gather 10.000 candies!
// Clicking the ‘Create candies’ button gives you 1 candy.
// You can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
// 10 lollipops generate 1 candy per second.
// Use the 🍭 emoji to display the lollipops you have
// Display the candy producton rate in the Candies / Second row
// If you press the "make candy rain" button, the candy generation should speed up 10x

// Candy counter
// Lollypop counter
//Something something timer

const time = 0;
let cadnys = 0;
let lollipops = 0;
let 


let time1Second = function (){
    time += 1;
    setTimeout(time1Second2, 1000);
}

let time1Second2 = function (){
    time += 1;
    setTimeout(time1Second, 1000);
}
setTimeout(time1Second, 1000);

let fast1Seond = function (){
    time += 1;
    setTimeout(fast1Seond2, 100);
}

let fast1Seond2 = function (){
    time += 1;
    setTimeout(fast1Second, 100);
}
