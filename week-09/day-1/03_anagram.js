// Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
// Create a test for that.

let anagram = function(string1, string2) {
    if (string1.length === string2.length) {
        string1.forEach(function(element){
            if (string2.includes(element)){

            } else {
                return false
            }
        })
    } else {
        return false
    }
}

console.log(anagram('cica', 'icca'));
