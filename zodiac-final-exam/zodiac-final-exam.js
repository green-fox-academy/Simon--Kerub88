// 5. Create a function that takes two arrays and decides if their content is the same

function isArraysMatch(list1, list2) {
    let newList2 = list2;
    if (list1.length === list2.length) {
        for (let i = 0; i < list1.length; i++){
            for (let j = 0; j < list1.length; j++){
                if (list1[i] === list2[j]){
                    newList2[j] = 0;
                }
                if (i === list1.length - 1) {
                    for (let n = 0; n < newList2.length; n++) {
                        if (newList2[n] !== 0) {
                            return false
                        } else {
                            return true
                        }
                    }
                }
            }
        }
    } else {
        return false
    }
}

console.log(isArraysMatch([5, 1, 2, 'a', 'b'], [1, 'b', 2, 'a', 5]));


// 3. Create a function that determines if a string is a palindrome

function palindrome(input){
    for (let i = input.length - 1, j = 0; i >= 0; i--, j++) {
        if (input[i] !== input[j]) {
            return false
        }
    }
    return true
}

console.log(palindrome('racecar'));
