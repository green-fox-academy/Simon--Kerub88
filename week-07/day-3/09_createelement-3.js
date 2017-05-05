// Remove the king from the list.
// Add list items that have the following text contents:
// ['apple', 'bubble', 'cat', 'green fox']

'use strict';

var daaaaList = document.querySelector('ul');
daaaaList.querySelector('li').remove();

////////////////////////////////////////////////

var newListItems = ['apple', 'bubble', 'cat', 'green fox']

for (var i = 0; i < newListItems.length; i++) {
    daaaaList.appendChild(document.createElement('li')).textContent = newListItems[i];
}
