// Three ways to write a function. But the way to call them is always the same.

// Function declaration
function sayHello1() {
    console.log("Hello 1");
}
sayHello1();

// Function expression
const sayHello2 = function() {
    console.log("Hello 2");
};
sayHello2();

// Arrow function (also a function expression)
const sayHello3 = () => {
    console.log("Hello 3");
};

sayHello1();
sayHello2();
sayHello3();