const isAdult = function (age) {
    if (age >= 18) {
        return true;
    }
    return false;
}

const doGreeting = function () {
    const checkIfAdult = isAdult(18);
    if (checkIfAdult === true) {
        return ("Hi There!");
    }
    return "Hey Kiddo"

}

console.log(doGreeting())

// **************************************************************

// VAT EXERCISE 1
calculateVat = function (basePrice, vat) {
    vat = 1 + (vat/100);
    return basePrice * vat;
}

totalPrice = function (price, vat) {
    return calculateVat(price, vat);

}

console.log(totalPrice(2, 9))

// **************************************************************

// VAT EXERCISE 2


calcBaseandVat = function (priceWVat, vat) {
    basePrice = priceWVat / (1 + (vat/100));
    vatAmount = priceWVat - basePrice;
    return [basePrice, vatAmount];
}

calculatePrice = function (totPrice, vat) {
    return calcBaseandVat(totPrice, vat);
}

console.log(calculatePrice(1210, 21))
console.log(calculatePrice(2.18, 9))