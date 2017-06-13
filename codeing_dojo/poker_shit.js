'use strict';

const value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
const colors = ['clubs', 'diamond', 'hearts', 'spades'];

const hand1 = ['2H', '3D', '5S', '9C', 'KD'];
const hand2 = ['2C', '3H', '4S', '8C', 'AH'];



var theHandJudge = (function(hand){

    let handInit = function(hand){
        var newHand = [];
        for (let i = 0; i < 5; i++) {
            let card = {
                'value': hand[i][0],
                'colors': hand[i][1]
            }
            newHand.push(card);
        }
        return newHand
    }

    var handStrength = {

        // let strength = 0;

        highCard: function(hand){
            return strength = 1;
        },

        pair: function(hand){
            return strength = 2;
        },

        twoPair: function(hand){
            return strength = 3;
        },

        threeOfAKind: function(hand){
            return strength = 4;
        },

        straight: function(hand){
            return strength = 5;
        },

        flush: function(hand){
            return strength = 6;
        },

        fullHouse: function(hand){
            return strength = 7;
        },

        fourOfAKind: function(hand){
            return strength = 8;
        },

        straightFlush: function(hand){
            return strength = 9;
        },

        royalFlush: function(hand){
            console.log('handlog',hand);
            if (hand[0].colors === hand[1].colors && hand[0].colors === hand[2].colors &&
            hand[0].colors === hand[3].colors && hand[0].colors === hand[4].colors) {
                let ace = 0;
                let jack = 0;
                let queen = 0;
                let king = 0;
                let ten = 0;
                hand.forEach(function(card){
                    if (card.value === 'A') {
                        ace++;
                    }
                    if (card.value === 'J') {
                        jack++;
                    }
                    if (card.value === 'Q') {
                        queen++;
                    }
                    if (card.value === 'K') {
                        king++;
                    }
                    if (card.value === 'T') {
                        ten++;
                    }
                })
                if (ace === 1 && jack === 1 && queen === 1 && king === 1 && ten === 1) {
                    let strength = 10;
                    return strength
                } else {
                    straightFlush(hand)
                }
            } else {
                fourOfAKind(hand)
            }
        }
    }
    return {
        handInit: handInit,
        handStrength: handStrength
    }
})()


// const value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
// const colors = ['clubs', 'diamond', 'hearts', 'spades'];
//
// const hand1 = ['2H', '3D', '5S', '9C', 'KD'];
// const hand2 = ['2C', '3H', '4S', '8C', 'AH'];

module.exports = theHandJudge;
