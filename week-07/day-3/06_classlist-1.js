    // Does the third p have a cat class?
    // If so, alert 'YEAH CAT!'
    // If the fourth p has a 'dolphin' class, replace apple's content with 'pear'
    // If the first p has an 'apple' class, replace cat's content with 'dog'
    // Make apple red
    // Make balloon less balloon-like
'use strict';
var classHolder = document.querySelectorAll('p');

if (classHolder[2].classList.contains('cat')) {
    window.alert('YEAH CAT!');
}

if (classHolder[3].classList.contains('dolphin')) {
    classHolder[0].innerHTML = 'pear';
}

if (classHolder[0].classList.contains('apple')) {
    classHolder[2].innerHTML = 'dog';
}

classHolder[0].style.color = 'red';
document.querySelector('.balloon').setAttribute('style', 'background-color: lime; border-radius: 0%;');
