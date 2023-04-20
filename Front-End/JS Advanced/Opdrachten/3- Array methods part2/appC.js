const containsNumberBiggerThan10 = function(array) {
    return array.some((number) => {
        return number > 10;
});
}
console.log(containsNumberBiggerThan10([1, 4, 3, 6, 9, 7, 11]))
// result should be true
console.log(containsNumberBiggerThan10([1,2,1,2,1,2]))
// result should be false