const bigSum = function(array) {
    const sum = array.reduce((accumulator, currentValue) => {
        return accumulator + currentValue;
    }, 0)

    return sum
}

// const bigSum = function(array) {
//      const sum = array.reduce((accumulator, currentValue) => {
//          return accumulator + currentValue);
//  }
// return sum


console.log(bigSum([1, 81, 4, 53, 3, 6, 79, 2, 43, 7, 28, 11, 77, 84, 98, 101, 206, 234]))
// result should be 1118