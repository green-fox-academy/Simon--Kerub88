'use strict';
// Join the two array by matching one girl with one boy in the order array
// Exepected output: ["Eve", "Joe", "Ashley", "Fred"...]

var girls = ["Eve","Ashley","Bözsi","Kat","Jane"];
var boys = ["Joe","Fred","Béla","Todd","Neef","Jeff"];

function matchmaking(girls, boys) {
    var order;
    var longList, shortList = [];
    if (girls.length > boys.length) {
        longList = girls;
        shortList = boys;
    }else {
        longList = boys;
        shortList = girls;
    }
    for (var i = 0; i < longList.length; i++) {
        if (i % 2 != 0) {
            longList.splice(i, 0, shortList.shift())
        }
    }
    order = longList
    return order
}


console.log(matchmaking(girls, boys));
