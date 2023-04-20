// Checking if a number is big

const isNumberBig = function(number) {
    if (number > 100) {
        return true;
    };
    return false;
};

console.log(isNumberBig(101));
console.log(isNumberBig(50));
console.log(isNumberBig(0));
console.log(isNumberBig(1111));


//  Bouncer at a club

const theBouncer = function(maxPeople, currentPeople, agePerson) {
    if (agePerson < 18) {
        return "This is a club fo adults";
    }
    if (currentPeople >= maxPeople) {
        return "It's too busy now, come back later";
    };
        return "Come in";
    
};


console.log(theBouncer(100, 0, 18));




// Calculating the average

const calcAverage = function(n1, n2, n3, n4, n5) {
    average = (n1 + n2 + n3 + n4 + n5) / 5
    return average
};

result5 = calcAverage(4, 5, 6, 8, 21);
console.log(result5);