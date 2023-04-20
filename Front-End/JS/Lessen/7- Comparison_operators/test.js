/*
Test this on the node.js terminal

var x = 5

 x > 4
true
 x > 5
false
 x  >= 4
true
 x < 5
false
 x == 4
false
 x == 5
true
 x === 5
true
 var = "5"
var = "5"

 x = "5"
'5'
x == 5
true
x === 5
false
x === '5'
true
x = 5
5
x != 4
true
x != 5
false
x !== 5
false
x = '5'
'5'
x !== 5
true
*/


// Example 1

/* 
var myAge = 25;

if (myAge >= 18 && myAge <= 30) {
    document.write("You can come, you cool dude!");

} else {

    document.write("You ain't coming!");
}
*/


// Example 2

var myAge = 35;

if (myAge < 18 || myAge > 30 || myAge === 25) {
    
    document.write("You ain't coming!");

} else {

    document.write("You can come, you cool dude!");
    
}