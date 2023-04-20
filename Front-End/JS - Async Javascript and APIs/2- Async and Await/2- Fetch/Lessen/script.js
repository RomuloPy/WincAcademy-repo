////// Use Fetch as a Promise: retrieve data from REST API //////

fetch("https://swapi.dev/api/people/1/")
    .then(response => response.json())
    .then(data => console.log(data)) 
    .catch(error => {
        console.log(error)
    });


///// Step 1: /////

// fetch("https://swapi.dev/api/people/1/") // make a request


///// Step 2: /////

// .then(response => response.json())

// Actually, it is very readable, fetch has a method (just like .map, .filter and .reduce methods are). 
// The method of fetch is .then().
// When the data is collected, you want to do something. That something is executed in the .then().
//In other words, you are going to do something when the fetch (Promise in disguise) is resolved.
// We now call whatever we get back from the server response. You convert your response to a json file with response.json().
// Why is this necessary? ⇒ The response you get contains a lot of extra (meta) data. The response data has not yet been converted to JSON*.
// JSON is the type of data we want and where we can get started.
// *unless you use an API that wants to know a very specific document format. That is not the case now.


// Step 3:

// .then(data => console.log(data)) 

// The next step is also a .then(), where you can do whatever you want with the data.
//In our particular case, we want to log the console.
//But you can also pass it to a function that puts it in the DOM, for example.


// Step 4:

// .catch(err => {
//         console.log(err)
//     });


// Remember, fetch is a promise in disguise. A promise may not be "resolved" (because the server is down, for example).
// Then you would like to know what the problem is.
// Besides then() fetch() has more methods. One of these is .catch().
// ****This method (literally) catches the error if the Promise is not resolved, but is rejected.
//If something goes wrong with your request, you want to know about it. That's why console.log gives you the error.