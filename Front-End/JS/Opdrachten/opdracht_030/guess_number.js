let numberToBeGuessed;
let userName;
let currentGuess;
let numberOfGuesses = 0;
let currentNumberOfGuesses = 5;
let minNum;
let maxNum;

const randomIntFromInterval = function(minNum, maxNum) { // min and max included 
    return Math.floor(Math.random() * (maxNum - minNum + 1) + minNum)
}


while (userName === undefined || userName === null || userName.length === 0) {
    userName = prompt("Welcome!What's your name?");
}
alert("Welcome to Guess The Number, " + userName + "!!");
minNum = prompt("Which is the smallest number to guess?");
maxNum = prompt("Which is the largest number to guess?");

while (numberOfGuesses < 5) {
    currentGuess = prompt(`Enter a number between ${minNum} and ${maxNum} to start guessing...`);
    numberToBeGuessed = randomIntFromInterval(minNum, maxNum);
    if (currentGuess != numberToBeGuessed) {
        alert(`Unfortunately, that is not correct! The number was ${numberToBeGuessed}. You still have ${currentNumberOfGuesses - 1} tries`);
    }
    else if (currentGuess != numberToBeGuessed) {
        alert("Congratulations, you have won the game!. The game is now finished.");
        break
    }
    numberOfGuesses++
    currentNumberOfGuesses--
    if (currentNumberOfGuesses === 0) {
        alert("You runned out of tries!")
        break
    }
}
alert(`Bye ${userName}, see you!`);
