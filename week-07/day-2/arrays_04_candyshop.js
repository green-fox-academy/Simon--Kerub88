'use strict';

var shop_items = ["Cupcake", 2, "Brownie", false]

// Accidentally we added "2" and "false" to the array.
// Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
// No, don't just remove the items :)

shop_items = shop_items.map(function(item){
    if (item === 2) {
        return 'Croissant'
    } else if (typeof(item) === 'boolean') {
        return 'Ice cream'
    } else {
        return item
    }
})
console.log(shop_items)
