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

let time = 0;
let candies = 0;
let lollypops = 0;
let fastTime = false;
let candiesSign = document.querySelector('.candies');
let lollypopsSign = document.querySelector('.lollypops');
let buttonCreatCandies = document.querySelector('.create-candies');
let buttonBuyLolypop = document.querySelector('.buy-lollypops');
let buttonCandyRain = document.querySelector('.candy-machine');


let addTime = function(){
    time += 1;
    console.log(time);
}

let timer = setInterval(addTime, 1000);

let timeSwitcher = function(){
    if (fastTime === false) {
        clearInterval(timer);
        timer = setInterval(addTime, 100);
        fastTime = true;
    } else if (fastTime === true) {
        clearInterval(timer);
        timer = setInterval(addTime, 1000);
        fastTime = false;
    }
}


let candieAdd = function(){
    candies += 1;
    candiesSign.innerHTML = candies;
}

let buyLollypop = function(){
    lollypops += 1;
    candies -= 100;
    lollypopsSign.innerHTML = lollypopsSign.innerHTML + '3C D8 6D DF';
}

buttonCandyRain.addEventListener('click', timeSwitcher);
buttonCreatCandies.addEventListener('click', candieAdd);
