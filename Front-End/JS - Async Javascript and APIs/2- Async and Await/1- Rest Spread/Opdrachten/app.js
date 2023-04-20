
// Function 1:

// Write a simple function that adds multiple numbers together
// The function accepts multiple arguments
// Use the rest parameter to make sure your function treats arguments as an array.

function sum(...numbers) {

    return numbers.reduce(
        (prev, current) => prev + current
    );
};

console.log(sum(4, 3, 8, 8, 9, 6));




////////////////////////////////////////////////////////////////////////////////////////////////

// Function 2:

// Write a simple function that adds multiple numbers together
// The function takes 1 argument, which is an array of numbers
// Use the spread operator to make sure your function sums up all items in the array.

function sum1(x, y) {
    
    return x + y;

}


let nums = [4, 3, 8, 8, 9, 6];

console.log(sum(...nums))