'use strict';

var buttonRight = document.querySelector('.right_button');
var buttonLeft = document.querySelector('.left_button');
var bckImage = document.querySelector('.background-image');
var mainImage = document.querySelector('img');
var currentImage = 0;

function changePictureRight(){
    if (currentImage < pictures.length - 1) {
        currentImage += 1;
    } else {
        currentImage = 0;
    }
    mainImage.setAttribute('src', pictures[currentImage].source);
    bckImage.style.backgroundImage = 'url(' + pictures[currentImage].source + ')';

}
function changePictureLeft(){
    if (currentImage > 0) {
        currentImage -= 1;
    } else {
        currentImage = pictures.length - 1;
    }
    mainImage.setAttribute('src', pictures[currentImage].source)
    bckImage.style.backgroundImage = 'url(' + pictures[currentImage].source + ')';
}

buttonLeft.addEventListener('click', changePictureLeft);
buttonRight.addEventListener('click', changePictureRight);



function checkKey(e) {
    if (e.keyCode == '37') {
        changePictureLeft();
       // left arrow
    }
    else if (e.keyCode == '39') {
        changePictureRight();
       // right arrow
    }

}

// document.onkeydown = checkKey;
document.addEventListener('keydown', checkKey)
