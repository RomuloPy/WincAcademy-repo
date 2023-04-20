const colors = ["yellow", "blue", "red", "orange"];
i = 0
while (i < colors.length) {
    console.log(colors[i]);
    i++
}

for (i = 0; i < colors.length; i++) {
    console.log(colors[i]);
}


/*************************************************************/ 

// Array.prototype.forEach()


colors.forEach(color => {
    console.log(color)});

/***************************************************************/

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