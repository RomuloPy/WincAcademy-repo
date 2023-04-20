  const doubleArrayValues = function (array) {
    let newArray = [];
    array.forEach(element => {
          newArray.push(element * 2);
      });
      console.log(newArray)
    
//  }

// const doubleArrayValues = function (array) {
//     values = array.map(integer => {
//         return integer*2;
//     })
//     console.log(values)
}

doubleArrayValues([1, 2, 3])
// result should be [2, 4, 6]
