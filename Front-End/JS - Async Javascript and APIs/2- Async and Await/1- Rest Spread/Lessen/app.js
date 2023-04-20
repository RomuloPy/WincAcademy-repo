// Rest Parameter - translates any sequence of arguments into an array

function sum(...numbers) {

    return numbers.reduce(function(prev, current) {

        return prev + current;
    });
}

/*  OR:
function sum(...numbers) {

    return numbers.reduce(
        (prev, current) => prev + current
    );
};
 

*/
console.log(sum(1, 2, 3));
console.log(sum(1, 2, 3, 4, 5));


///////////////////////////////////////////////////////////////////////

// Spread Operator - split an array into a sequence of arguments(function)

function sum1(x, y) { // 1, 2
    
    return x +y;

}


let nums = [1, 2];

console.log(sum(...nums))