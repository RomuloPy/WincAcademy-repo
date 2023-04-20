/*
Exercise 2:
Write two functions that use Promises that you can chain!
The first function, makeAllCaps(), will take in an array of words and capitalize them, and then the second function, sortWords(),
will sort the words in alphabetical order. If the array contains anything but strings, it should throw an error.
Then call these functions by *chaining* the promises
*/

const makeAllCaps = words => {
    return new Promise((resolve, reject) => {
        if (
            words.every(word => {
                return typeof word === 'string';
            })
        ) {
            resolve(
                sortWords(
                    words.map(word => {
                        return word.toUpperCase();
                })
            )
        );
        } else {
            reject( 'Not a string!');
        }     
    });
};  

const sortWords = words => {
    return new Promise((resolve, reject) => {
        if (words) {
            resolve(words.sort());
        } else {
            reject('strings only!');
        }
    });
};


const arrayOfWords = ['cucumber', 'tomatos', 'avocado'];
const complicatedArray = ['cucumber', 44, true];

// call both functions, chain them together and log the result to the console

makeAllCaps(arrayOfWords)
    .then(sortWords(arrayOfWords))
    .then(result => console.log(result))
    .catch(error => console.log(error))


makeAllCaps(complicatedArray)
.then(sortWords(complicatedArray))
.then(result => console.log(result))
.catch(error => console.log(error))