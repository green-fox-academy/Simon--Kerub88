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
let lollipops = 0;
let fastTime = false;
let candiesSign = document.querySelector('.candies');
let buttonCreatCandies = document.querySelector('.create-candies');
let buttonBuyLolypop = document.querySelector('.buy-lollypops');
let buttonCandyRain = document.querySelector('.candy-machine');


let time1Second = function (){
    if (fastTime === false){
        time += 1;
        console.log(time);
        setTimeout(time1Second2, 1000);
    } else {
        fast1Second();
    }
}

let time1Second2 = function (){
    if (fastTime === false){
        time += 1;
        console.log(time);
        setTimeout(time1Second, 1000);
    } else {
        fast1Second();
    }
}
setTimeout(time1Second, 1000);

let fast1Seond = function (){
    if (fastTime === true){
        time += 1;
        console.log(time);
        setTimeout(fast1Seond2, 100);
    } else {
        setTimeout(time1Second, 900)
        fastTime = false;
    }
}

let fast1Seond2 = function (){
    if (fastTime === true){
        time += 1;
        console.log(time);
        setTimeout(fast1Seond, 100);
    } else {
        setTimeout(time1Second, 900)
        fastTime = false;
    }
}

let candieAdd = function(){
    candies += 1;
    candiesSign.innerHTML = candies;

}

let candieRainSwitch = function(){
    if (fastTime = false) {
        fastTime = true;
        console.log('Eddig lassan telt az ido, most felgyorsul. fastTime = ' + fastTime)
        fast1Seond();
    } else if (fastTime = true){
        fastTime = false;
        console.log('Eddig gyorsan telt az ido, most lelassul. fastTime = ' + fastTime)
        time1Second();
    }
}


buttonCandyRain.addEventListener('click', candieRainSwitch)
buttonCreatCandies.addEventListener('click', candieAdd);
