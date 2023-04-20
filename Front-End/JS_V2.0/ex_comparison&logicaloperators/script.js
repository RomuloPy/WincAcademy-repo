let myAge = 20
const firstName = "Bram"
const totalAmount = 10

if (myAge >= 18 && myAge <= 25) {

    console.log("You get 50% off");

} else {

    console.log("You'll not get a discount!");

}

if (firstName === "Sarah" || firstName === "Bram") {

    console.log("Free beer!!!");

} else

if (totalAmount > 25) {

    console.log("You get free (veggie) bitterballen!");

} else if (totalAmount > 50) {

    console.log("You get a free portion of nachos!");

} else if (totalAmount >= 100) {

    console.log("You get a free bottle of champagne!");

} else {

    console.log("No extra present for you...")
}