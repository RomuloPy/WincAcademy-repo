const age = 25;
const isFemale = false;
const driverStatus = "bob"
const firstName = "Sara"
const totalAmount = 100

// Use the data here under, to test the opposite values:
/*const age = 15;
const isFemale = true;
const driverStatus = "non-bob"
*/

if (age >= 18) {
    console.log("You're allowed to come in our bar, Welcome!")

} else {
    console.log("You're under 18 years old, we are sorry but you can't come inside our bar.")
}

if (age >= 18 && age <= 25) {
    console.log("You get 50% off!")

} else {
    console.log("You don't get any discount!")
}

if (isFemale) {
    console.log("Welcome to the ladies night :) ")

} else{
    console.log("We're sorry but today is ladies night, no men allowed :( ")
}

if (driverStatus == "bob") {
    console.log("You are the 'bob' tonight, so you may drive.")

} else{
    console.log("You're not 'bob' so you can't drive. Do not drive after drink alcohol!")
}

if (firstName == 'Bram' || firstName == 'Sarah') {
    console.log("You get free beer!")
} else {
    console.log("Only Bram and Sarah get free beer today!")
}

if (totalAmount >= 100) {
    console.log("You get a free bottle of champagne");
  } else if (totalAmount > 50) {
    console.log("You get a free portion of nachos!");
  } else if (totalAmount > 25) {
    console.log("You get free (veggie) Bitterballen!");
  } else {
    console.log("Unfortunately you don't get any discount...");
  }