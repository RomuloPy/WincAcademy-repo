function squareAdd(num1, num2) {
    square = (num1 * num1) + (num2 * num2);
    square1 = (square * square);
    return square1;
};

console.log(squareAdd(2, 3));


const squareAdd1 = function(num3, num4) {
    square2 = (num3 * num3) + (num4 * num4);
    square3 = (square2 * square2);
    return square3;
};

console.log(squareAdd1(2, 3));


const squareAdd2 = (num5, num6) => {
    square4 = (num5 * num5) + (num6 * num6);
    square5 = (square4 * square4);
    return square5;
}

console.log(squareAdd2(2, 3));
