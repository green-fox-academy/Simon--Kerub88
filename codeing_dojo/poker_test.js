'use strict';

// http://codingdojo.org/kata/PokerHands/

let test = require('tape');
let theHandJudge = require('./poker_shit.js');

test('create new hand from the card codes', function (t){
    let testHand = ['2H', '3D', '5S', '9C', 'KD'];
    let newHandShouldBe = [ { value: '2', colors: 'H' },
      { value: '3', colors: 'D' },
      { value: '5', colors: 'S' },
      { value: '9', colors: 'C' },
      { value: 'K', colors: 'D'}]
    t.deepEqual(theHandJudge.handInit(testHand), newHandShouldBe);
    t.end();
});

test('recognize a royal flush', function (t){
    let testHand = ['TC', 'JC', 'QC', 'KC', 'AC'];
    let newTestHand = theHandJudge.handInit(testHand);
    let strength = 10;
    t.equal(theHandJudge.handStrength.royalFlush(newTestHand), strength);
    t.end();
});
