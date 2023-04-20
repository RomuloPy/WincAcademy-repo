// Part 1 Objects

// 1.2.
let person = {
    name: 'Rómulo',
    age: 43
};

// 3.
console.log(person);

//4.
console.log(person.name);

// 5.
console.log(person.age);

// 6.
person.name = 'Santos';
console.log(person.name);
person['name'] = 'Rómulo';
console.log(person.name);

// 7.
let evaluations = [7, 9, 10];

// 8.
console.log(person.evaluations);



// Part 2 Arrays

// 1.
let myColors = []

// 2.
myColors[0] = 'green';
myColors[1] = 'blue';
myColors[2] = 'red';

// 3.
console.log(myColors);

// 4.
console.log(myColors.length);

// 5.
console.log(myColors[0]);

// 6.
console.log(myColors[myColors.length - 1]);

// 7.
myColors.push('Yellow');

// 8.
myColors.push(5);

// 9.
let hello = {
    greeting: "hi, I'm an object"
};

myColors.push(hello);
console.log(myColors[myColors.length - 1]);


// Part 3 A "real-life" object

const catBreeds = [{
    name: "Abyssinian",
    description: "The Abyssinian is easy to care for, and a joy to have in your home. They’re affectionate cats and love both people and other animals.",
    dog_friendly: 4,
    energy_level: 5,
    life_span: "14 - 15",
    origin: "Egypt",
    temperament: ["Active", "Energetic", "Independent", "Intelligent", "Gentle"],
    wikipedia_url: "https://en.wikipedia.org/wiki/Abyssinian_(cat)",
    food: {
        favourite_food: "fish",
        medium_liked_food: "dried fruits",
        disliked_food: "walnuts"
    }
},
{
    name: "Aegean",
    description: "Native to the Greek islands known as the Cyclades in the Aegean Sea, these are natural cats, meaning they developed without humans getting involved in their breeding. As a breed, Aegean Cats are rare, although they are numerous on their home islands. They are generally friendly toward people and can be excellent cats for families with children.",
    dog_friendly: 4,
    energy_level: 53,
    life_span: "9- 12",
    origin: "Greece",
    temperament: ["Affectionate", "Social", "Intelligent", "Playful", "Active"],
    wikipedia_url: "https://en.wikipedia.org/wiki/Aegean_cat",
    food: {
        favourite_food: "tuna",
        medium_liked_food: "canned food",
        disliked_food: "all fruits"
    }
},
{
    name: "American Bobtail",
    description: "American Bobtails are loving and incredibly intelligent cats possessing a distinctive wild appearance. They are extremely interactive cats that bond with their human family with great devotion.",
    dog_friendly: 5,
    energy_level: 3,
    life_span: "11 - 15",
    origin: "United States",
    temperament: ["Intelligent", "Interactive", "Lively", "Playful", "Sensitive"],
    wikipedia_url: "https://en.wikipedia.org/wiki/American_Bobtail",
    food: {
        favourite_food: "meaty things",
        medium_liked_food: "tuna",
        disliked_food: "canned food"
    }
}
];

// 1.
console.log("Name cat breed 3:", catBreeds[2].name);

// 2.
console.log("Energy level cat breed 1:", catBreeds[0].energy_level);

// 3.
console.log("First temperament cat breed 2:", catBreeds[1].temperament[0]);

// 4.
const lengthTemperamentCatThree = catBreeds[2].temperament.length;
console.log("Last temperament cat breed 3:", catBreeds[2].temperament[lengthTemperamentCatThree -1]);

// 5.
console.log("Favorite food cat breed 3:", catBreeds[2].food.favourite_food);