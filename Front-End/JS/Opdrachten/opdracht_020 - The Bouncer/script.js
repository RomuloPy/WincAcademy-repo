const age = 21;
const isFemale = false;
const driverStatus = "bob"

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