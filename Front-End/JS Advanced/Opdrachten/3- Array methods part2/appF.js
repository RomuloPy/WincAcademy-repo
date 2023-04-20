
const isBelow100 = function(array) {
    return array.every((element) => {
        return element < 100

    })
}

console.log(isBelow100([1, 81, 4, 53, 3, 6, 79, 2, 43, 7, 28, 101, 11, 77, 84, 98 ]))
// result should be: false