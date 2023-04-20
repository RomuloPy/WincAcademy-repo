const tenfold = function(array) {
    let newArray = [];
    array.forEach((element) => {
        newArray.push(element*10)
    });
    return newArray
    
}



console.log(tenfold([1, 4, 3, 6, 9, 7, 11]))
// result should be [10, 40, 30, 60, 90, 70, 110]


const tenfoldMap = function(array) {
    return array.map((element) => {
        return element * 10
    })
}
console.log(tenfoldMap([1, 4, 3, 6, 9, 7, 11]))