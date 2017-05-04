'use strict';

// <!-- You can work in the html or in a separate js file. Like:
// <script>
//   1. store the element that says 'The King' in the 'king' variable.
//   console.log it.
//   2. store the element that contains the text 'The Conceited Man'
//   in the 'conceited' variable.
//   show the result in an 'alert' window.
//   3. store 'The Businessman' and 'The Lamplighter'
//   in the 'businessLamp' variable.
//   console.log each of them.
//   4. store 'The King' and 'The Conceited Man'
//   in the 'conceitedKing' variable.
//   alert them one by one.
//   5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
//   in the 'noBusiness' variable.
//   console.log each of them.
//   6. store 'The Businessman' in the 'allBizniss' variable.
//   show the result in an 'alert' window.
// </script>

var king = document.getElementById('b325');
var conceited = document.querySelector('.b326');
// window.alert(conceited.innerHTML);
var businessLamp = document.querySelectorAll('.big');
console.log(businessLamp[0], businessLamp[1]);
var conceitedKing = document.getElementsByClassName('asteroid');
console.log(conceitedKing);
var conceitedKing2 = []
for (var i = 0; i < 2; i++) {
    console.log(conceitedKing[i])
    conceitedKing2.push(conceitedKing[i])
}
console.log(conceitedKing2)

var conceitedKing3 = document.querySelectorAll('section .asteroid')
console.log(conceitedKing3)
// window.alert(conceitedKing3[0].innerText)
// window.alert(conceitedKing3[1].innerText)

var noBusiness = document.querySelectorAll('div');
console.log(noBusiness[0])
console.log(noBusiness[1])
console.log(noBusiness[2])

var allBizniss = document.querySelector('p');

window.alert(allBizniss);
