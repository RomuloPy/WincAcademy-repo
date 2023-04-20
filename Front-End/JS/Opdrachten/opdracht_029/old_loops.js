const myColorsArray = ["yellow", "blue", "red", "orange"];

// old style

var i = 0;

while (i < myColorsArray.length) {
    console.log(myColorsArray[i]);
    i++
}


for (var i = 0; i < myColorsArray.length; i++) {
    console.log(myColorsArray[i])
}


// new style using forEach

myColorsArray.forEach(color => console.log(color));

// 1. The for loop is 3 lines, the while loop is 5 lines1
// 2. The forEach way is 1 line.
// 3. Array methods have the following advantages
// --> it's harder to get into an infinite loop
// --> you don't have to "manually" remember which iteration of the loop you're in with an index variable like "i".
// --> you immediately get the "thing" you're interested in, you do not have to manually grab it from the array
// --> the name forEach is more easily readable and understandable

const myColors = {
    colorWall: "blue",
    colorFruit: "orange",
    colorCar: "red",
    colorHair: "white",
    colorGras: "green",
};

for (let property in myColors) {
    console.log(myColors[property]);
}

// Yes, you're iterating now. But you're iterating over the *properties* of an
// object, not directly over the object.
// Only arrays have array methods.