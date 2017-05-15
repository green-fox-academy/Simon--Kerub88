'use strict';
// Create a sum method in your class which has a list of integers as parameter
// It should return the sum of the elements in the list
    // Follow these steps:
    // Add a new test case
    // Instantiate your class
    // create a list of integers
// use the t.equal to test the result of the created sum method
// Run it
// Create different tests where you
    // test your method with an empyt list
    // with a list with one element in it
    // with multiple elements in it
    // with a null
    // with a string
// Run them
// Fix your code if needed

var test = require('tape');
var sumArrays = require('./02_sum.js');

// with multiple elements in it
test('array with numbers as argument', function(t){
    var actual = sumArrays([2, 5, 6, 1]);
    var expected = 14;

    t.equal(actual, expected);
    t.end();
})

// test your method with an empyt list
test('empty array as argument', function(t){
    var actual = sumArrays([]);
    var expected = 0;

    t.equal(actual, expected);
    t.end();
})

// with a list with one element in it
test('array with one number', function(t){
    var actual = sumArrays([2]);
    var expected = 2;

    t.equal(actual, expected);
    t.end();
})

// with a null
test('array with a zero', function(t){
    var actual = sumArrays([0]);
    var expected = 0;

    t.equal(actual, expected);
    t.end();
})

// with a string
test('array with string elements', function(t){
    var actual = sumArrays([1, 3, 'ten']);
    var expected = 'One or more element of the array is not a number'

    t.equal(actual, expected);
    t.end();
})
