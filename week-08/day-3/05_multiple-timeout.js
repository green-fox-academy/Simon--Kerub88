'use strict';

// Write a program that prints the following fruits:
// apple -> immediately
// pear -> after 1 seconds
// melon -> after 3 seconds
// grapes -> after 5 seconds

function apple(){
    console.log('apple');
}

function pear(){
    console.log('pear');
}

function melon(){
    console.log('melon');
}

function grapes(){
    console.log('grapes');
}

apple();
setTimeout(melon, 3000);
setTimeout(pear, 1000);
setTimeout(grapes, 5000);
