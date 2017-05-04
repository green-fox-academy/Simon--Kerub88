// Add an item that says 'The Green Fox' to the asteroid list.
//    Add an item that says 'The Lamplighter' to the asteroid list.
//    Add a heading saying 'I can add elements to the DOM!' to the .container.
//    Add an image, any image, to the container.
'use strict';

var asteroidContainer = document.querySelector('ul');

var newAsteroid = document.createElement('li');
newAsteroid.textContent = 'The Green Fox';
asteroidContainer.appendChild(newAsteroid);
var newAsteroid2 = document.createElement('li');
newAsteroid2.textContent = 'The Lamplighter';
asteroidContainer.appendChild(newAsteroid2);
var creatHeading = document.createElement('h1');
creatHeading.textContent = 'I can add elements to the DOM!'
document.querySelector('.container').appendChild(creatHeading);
var newImg = document.createElement('img')
newImg.setAttribute('src', 'http://piq.codeus.net/static/media/userpics/piq_132922_400x400.png');
document.querySelector('.container').appendChild(newImg);
