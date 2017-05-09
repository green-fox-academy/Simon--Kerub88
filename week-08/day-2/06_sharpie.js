// Create a Sharpie constructor
//
// We should know about each sharpie their color (which should be a string), width (which will be a floating point number), inkAmount (another floating point number)
// When creating one, we need to specify the color and the width
// Every sharpie is created with a default 100 as inkAmount
// We can use() the sharpie objects
// which decreases inkAmount by the width

let sharpieConstructor = function(color, width, inkAmount) {
    let sharpie = {
        color: color,
        width: width,
        inkAmount: inkAmount,
    }
    return sharpie
}

let sharpieGreen = sharpieConstructor('green', 0.4, 100);
console.log(sharpieGreen);
let sharpieBlue = sharpieConstructor('blue', 0.2, 100);
console.log(sharpieBlue);
let sharpieOrange = sharpieConstructor('orange', 0.5, 100);
console.log(sharpieOrange);

function use() {
    this.inkAmount -= this.width;
    console.log(this.color + ' sharpies ink amount is: ' + this.inkAmount);
}

(use.bind(sharpieGreen))();
(use.bind(sharpieBlue))();
(use.bind(sharpieOrange))();
