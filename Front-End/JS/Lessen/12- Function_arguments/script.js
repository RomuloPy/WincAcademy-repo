const heat = function (item) {
    console.log("I'm heating " + item);
    console.log("Ping! Your " + item + " is heated");
};

const main_course = "pasta";
const dessert = "cake";

heat("popcorn");
heat("cauliflower");

heat(main_course);
heat(dessert);



// Arguments

const multiply = function (numberA, numberB) {
    console.log(numberA * numberB);
};

multiply(3, 4);


const dogAge = 5;
const dogYearsFactor = 7;

multiply(dogAge, dogYearsFactor);


const calculateAverage = function (numbers) {
    // calculate average
    const average = numbers.reduce((total, n) => total + n) / numbers.length;
    console.log(average)
};

const grades = [6, 7, 8, 9, 5, 6, 7, 8];
calculateAverage(grades);

const ages = [16, 22, 50, 100, 34];
calculateAverage(ages);