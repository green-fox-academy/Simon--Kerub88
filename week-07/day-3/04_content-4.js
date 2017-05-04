    // replace the list items' content with items from this list:
    // ['apple', 'banana', 'cat', 'dog']

var listItems = ['apple', 'banana', 'cat', 'dog'];

var list = document.querySelectorAll('li');
console.log(list)
console.log(list[1].innerHTML)

list.forEach(function(i, ind){
    i.innerHTML = listItems[ind];
})
