'use strict';
// Remove the king from the list.
// Add 3 list items saying 'The Fox' to the list.

var daaaList = document.querySelector('ul');
daaaList.querySelector('li').remove();

for (var i = 0; i < 3; i++){
    var newLi = document.createElement('li');
    daaaList.appendChild(newLi).textContent = 'The Fox';
}
