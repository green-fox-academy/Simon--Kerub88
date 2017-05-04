// Write the image's url to the console.
// Replace the image with a picture of yourself.
// Make the link point to the Green Fox Academy website.
// Disable the second button.
// Replace its text with 'Don't click me!'.

var imgUrl = document.querySelector('img');
console.log(imgUrl.getAttribute('src'));
imgUrl.setAttribute('src', 'http://i.imgur.com/z0pGqEM.jpg');

document.querySelector('a').setAttribute('href', 'https://www.greenfoxacademy.com/');

document.querySelectorAll('button')[1].disabled = true;
document.querySelectorAll('button')[1].innerText = "Don't click me!";
