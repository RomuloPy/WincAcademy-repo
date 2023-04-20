/*
- return inside a function
- return keyword vs return statement
- how does it work?
    - stop function
    - go back to where function was called
    - return value
- what can I return?
- multiple return values
- all functions return "something"
*/

const add = function(number1, number2) {
    const sum = number1 + number2;
    if (sum > 10) {
        return sum;
    }
    return "too low";
};

const result = add(6, 5);
console.log(result);

const result1 = add(4, 5);
console.log(result1);

const doubleArray = function(numbers) {
    const doubled = numbers.map(n => n * 2);
    return doubled;
};

const result2 = doubleArray([1, 2, 3]);
console.log(result2);


const scream = function(sentence) {
    console.log(`${sentence}!!!`);
};

const result3 = scream("Bees");
console.log(result3);