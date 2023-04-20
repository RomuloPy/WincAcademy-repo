const isBigger = function (number) {
    
    if (number > 100) {
        return true
    }
    return false
}
 // OR

const isBigger1 = function(number) {
    return number > 100;
}
console.log(isBigger1(10));
console.log(isBigger1(90));
console.log(isBigger1(99));
console.log(isBigger1(100));
console.log(isBigger1(101));

// **************************************************************

const aiBouncer = function (maxPeople, currPeople, agePerson) {

    if (currPeople <= 100 && agePerson >= 18 && currPeople < 100) {
        return ("Come in")
    }
    else if (currPeople === maxPeople) {
        return ("It's too busy now, come back later")
    }
    else if (agePerson < 18) {
        return ("This is a club for adults")
    }

}

console.log(aiBouncer(100, 100, 15))


// ***************************************************************

const average = function (
    num1, 
    num2, 
    num3, 
    num4, 
    num5
) {

    result = Math.round((num1 + num2 + num3 + num4 + num5) / 5)
    return result

}



console.log(average(4, 7, 8, 5, 7));