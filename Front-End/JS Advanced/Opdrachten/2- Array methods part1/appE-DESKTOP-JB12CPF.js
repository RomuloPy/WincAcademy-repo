const presidents = ["Trump", "Obama", "Bush", "Clinton"] 

const impeachTrumpSlice = function(array) {
    trump = presidents.slice(1);
    return trump
}
const impeachTrumpSplice = function(array) {
    presidents.splice(0, 1)
    return presidents
}

console.log(impeachTrumpSlice(presidents)); // ["Obama", "Bush", "Clinton"]
console.log(impeachTrumpSplice(presidents)); // ["Obama", "Bush", "Clinton"]