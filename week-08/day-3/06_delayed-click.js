'use strict';

// <!-- Create a simple HTML document with one button.
// If the user clicks the button it should wait 2 seconds and
// it should show a text under the button: 2 seconds ellapsed -->

let button = document.querySelector('button');
button.addEventListener('click', creatText)

function creatText(){
    var theCreator = function(){
        let h1 = document.createElement('h1');
        h1.innerHTML = '2 seconds ellapsed';
        document.body.appendChild(h1);
    }
    setTimeout(theCreator, 2000)
}
