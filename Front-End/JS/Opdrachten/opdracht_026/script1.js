const doubleSquare = function (number1, number2) {

    squNumber1 = number1 * number1;
    squNumber2 = number2 * number2;
    add1 = squNumber1 + squNumber2;
    squAdd1 = add1 * add1;
    return squAdd1
}



//*****************************************************

function doubleSquare1(number3, number4) {

    squNumber3 = number3 * number3;
    squNumber4 = number4 * number4;
    add2 = squNumber3 + squNumber4;
    squAdd2 = add2 * add2;
    return squAdd2
}



//*****************************************************

const doubleSquare2 = (number5, number6) => {

    squNumber5 = number5 * number5;
    squNumber6 = number6 * number6;
    add3 = squNumber5 + squNumber6;
    squAdd3 = add3 * add3;
    return squAdd3

}


console.log(doubleSquare(2, 3));
console.log(doubleSquare1(2, 3));
console.log(doubleSquare2(2, 3));