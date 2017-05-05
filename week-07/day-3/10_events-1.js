// Turn the party on and off by clicking the button.
'use strict';

var button = document.querySelector('button');
function partyStarter() {

    document.querySelector('div').className += 'party';
}
button.addEventListener('click', partyStarter);
