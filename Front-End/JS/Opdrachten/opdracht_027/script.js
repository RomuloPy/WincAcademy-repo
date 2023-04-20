// Hey kiddo

const adultCheck = function (age) {
    if (age >= 18) {
        return true;
    };
    return false;
};

function greet() {
    check = adultCheck(20);
    if (check === true) {
        return "Hello there!"
    };
    return "Hey kiddo!";

};

console.log(greet());



// VAT calculations

// Exercise 1

function priceTotal1(base_Price1, vatPercentage1) {
    price_Calculation1 = (base_Price1 * vat_Calculation1());
    return price_Calculation1;
    function vat_Calculation1() {
        calculation1 = (vatPercentage1 + 100) / 100
        return calculation1
    };
};

console.log(priceTotal1(1000, 19))


// Exercise 2

function calculateBase_price_and_vatAmount(priceTotal2, vatPercentage2) {
    base_Price2 = priceTotal2 / vat_Calculation2()
    vatAmount = priceTotal2 - base_Price2
    return [base_Price2, vatAmount];

    function vat_Calculation2() {
        calculation2 = (vatPercentage2 + 100) / 100;
        return calculation2;
    };
};

console.log(calculateBase_price_and_vatAmount(393.25, 21));
