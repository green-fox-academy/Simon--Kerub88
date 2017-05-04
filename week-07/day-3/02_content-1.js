// <!-- You can work in the html or in a separate js file.
// Like:
//   <script>
//     1. Alert the content of the heading.
//     2. Write the content of the first paragraph to the console.
//     3. Alert the content of the second paragraph.
//     4. Replace the heading's content with 'New content'.
//     5. Replace the last paragraph's content with the first paragraph's content.
//   </script>
var h1Var = document.querySelector('h1');
console.log(h1Var);

window.alert(h1Var.innerHTML)

window.alert(document.querySelectorAll('p')[0].innerHTML);

h1Var.innerHTML = 'New Content'

document.querySelectorAll('p')[2].innerHTML = document.querySelectorAll('p')[0].innerHTML;
console.log(document.querySelectorAll('p')[2].innerHTML)
