// <script>
//   fill every paragraph with the last one's content.
// </script>


var paragraph = document.querySelectorAll('p');
console.log(paragraph)
paragraph.forEach(function(i) {
    i.innerHTML = paragraph[3].innerHTML
})
