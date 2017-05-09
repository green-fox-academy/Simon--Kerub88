// Create an Animal constructor
//
// Every animal has a hunger value, which is a number
// Every animal has a thirst value, which is a number
// when creating a new animal object these values are created with the default 50 value
// Every animal can eat() which decreases their hunger by one
// Every animal can drink() which decreases their thirst by one
// Every animal can play() which increases both by one
// Create a Farm constructor
//
// Every farm has list of Animals
// Every farm has slots which defines the number of free places for animals
// Every farm can breed() which creates a new animal if there's place for it
// Every farm can slaughter() which removes the least hungry animal

'use strict';

const AnimalConstructor = function(){
    let animal = {
        hunger: 50,
        thirst: 50,
        eat: function(){
            this.hunger -= 1;
        },
        drink: function(){
            this.thirst -= 1;
        },
        play: function(){
            this.hunger += 1;
            this.thirst += 1;
        },
    }
    return animal
}

const FarmConstructor = function(){
    let farm = {
        listOfAnimals: [],
        freeSlots: 5,
        breed: function(){
            if (this.freeSlots > 0) {
                this.freeSlots -= 1;
                this.listOfAnimals.push(AnimalConstructor());
            }
        },
        slaughter: function(){
            this.listOfAnimals.sort(function(a, b){
                return a.hunger - b.hunger
            });
            this.listOfAnimals.shift();

        }
    }
    return farm
}

let farm1 = FarmConstructor();
farm1.breed();
farm1.breed();
farm1.breed();
farm1.breed();
farm1.listOfAnimals[1].eat();
farm1.listOfAnimals[1].eat();
farm1.listOfAnimals[1].eat();
farm1.listOfAnimals[2].eat();
farm1.listOfAnimals[2].eat();
farm1.listOfAnimals[3].eat();

console.log(farm1.listOfAnimals[0].hunger);
farm1.slaughter();
console.log(farm1.listOfAnimals);
