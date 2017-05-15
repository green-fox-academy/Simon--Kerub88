'use strict';
// Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
// Create a test for that.


var test = require('tape');
var anagram = require('./03_anagram.js');


test('2 string', function(t){
    var actual = anagram('kaloz', 'zolak');
    var expected = true;

    t.equal(actual, expected);
    t.end();
})

test('uppercase and lowercase', function(t){
    var actual = anagram('kAlOz', 'zolak');
    var expected = true;

    t.equal(actual, expected);
    t.end();
})
