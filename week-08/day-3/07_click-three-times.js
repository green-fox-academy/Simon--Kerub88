'use strict';
// Click Three Times
//
// Create a simple HTML document with one button. If the user clicks the button 3 times, and 5 seconds is already ellapsed since the page is loaded, a text should apper under the button: 5 seconds ellapsed and clicked 3 times

const button = document.querySelector('button');
const h1 = document.querySelector('h1');
let buttonClicked = 0;
let timeIsReady = false;

let timer = function(){
    if (buttonClicked >= 3){
        textSign();

    }else {
        timeIsReady = true;

    }
}

let textSign = function(){
    h1.innerHTML = '5 seconds ellapsed and clicked 3 times';
}

let buttonChecker = function(){
    if (buttonClicked <= 3){
        buttonClicked += 1;

    } else if ((buttonClicked >= 3) && (timeIsReady === true)){
        textSign();
    }
}

setTimeout(timer, 5000);

button.addEventListener('click', buttonChecker);
