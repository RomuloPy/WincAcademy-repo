const myColors = []

myColors[0] = "green"
myColors[1] = "blue"
myColors[2] = "red"

console.log(myColors);
console.log(myColors.length);
console.log(myColors[0]);
console.log(myColors[myColors.length -1]);

myColors.push("Yellow");
console.log(myColors);

myColors.push(5);
console.log(myColors);

myColors.push({greeting: "Hi, I am an object"});
console.log(myColors);

console.log(myColors[myColors.length -1].greeting);