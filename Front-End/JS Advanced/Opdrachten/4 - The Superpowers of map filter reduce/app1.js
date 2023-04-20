const superheroes = [
    {
    name: "Batman",
    publisher: "DC Comics",
    alter_ego: "Bruce Wayne",
    first_appearance: "Detective Comics #27",
    weight: "210"
    },
    {
    name: "Superman",
    publisher: "DC Comics",
    alter_ego: "Kal-El",
    first_appearance: "Action Comics #1",
    weight: "220"
    },
    {
    name: "Flash",
    publisher: "DC Comics",
    alter_ego: "Jay Garrick",
    first_appearance: "Flash Comics #1",
    weight: "195"
    },
    {
    name: "Green Lantern",
    publisher: "DC Comics",
    alter_ego: "Alan Scott",
    first_appearance: "All-American Comics #16",
    weight: "186"
    },
    {
    name: "Green Arrow",
    publisher: "DC Comics",
    alter_ego: "Oliver Queen",
    first_appearance: "All-American Comics #16",
    weight: "195"
    },
    {
    name: "Wonder Woman",
    publisher: "DC Comics",
    alter_ego: "Princess Diana",
    first_appearance: "The Incredible Hulk #180",
    weight: "165"
    },
    {
    name: "Blue Beetle",
    publisher: "DC Comics",
    alter_ego: "Dan Garret",
    first_appearance: "Mystery Men Comics #1",
    weight: "145"
    },
    {
    name: "Spider Man",
    publisher: "Marvel Comics",
    alter_ego: "Peter Parker",
    first_appearance: "Amazing Fantasy #15",
    weight: "167"
    },
    {
    name: "Captain America",
    publisher: "Marvel Comics",
    alter_ego: "Steve Rogers",
    first_appearance: "Captain America Comics #1",
    weight: "220"
    },
    {
    name: "Iron Man",
    publisher: "Marvel Comics",
    alter_ego: "Tony Stark",
    first_appearance: "Tales of Suspense #39",
    weight: "250"
    },
    {
    name: "Thor",
    publisher: "Marvel Comics",
    alter_ego: "Thor Odinson",
    first_appearance: "Journey into Myster #83",
    weight: "200"
    },
    {
    name: "Hulk",
    publisher: "Marvel Comics",
    alter_ego: "Bruce Banner",
    first_appearance: "The Incredible Hulk #1",
    weight: "1400"
    },
    {
    name: "Wolverine",
    publisher: "Marvel Comics",
    alter_ego: "James Howlett",
    first_appearance: "The Incredible Hulk #180",
    weight: "200"
    },
    {
    name: "Daredevil",
    publisher: "Marvel Comics",
    alter_ego: "Matthew Michael Murdock",
    first_appearance: "Daredevil #1",
    weight: "200"
    },
    {
    name: "Silver Surfer",
    publisher: "Marvel Comics",
    alter_ego: "Norrin Radd",
    first_appearance: "The Fantastic Four #48",
    weight: "unknown"
    }
    ]


//    1. Make an array of all superhero names.

let allSuperheroeNames = superheroes.map((hero) => {
    return hero.name
});

console.log("1. All superheroes names:", allSuperheroeNames)

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 2. Make an array of all "light" superheroes (< 190 pounds)

const lightOnes = superheroes.filter(hero => {
    return hero.weight < 190;
})


console.log("2. Light superheroes:", lightOnes)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 3. Create an array with the names of the superheroes who weigh 200 pounds

const twoHundredPounds = superheroes
    .filter(hero => hero.weight == 200)
    .map(hero => hero.name);


console.log("3. Heroes with 200 pounds:", twoHundredPounds)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 4. Make an array with all the comics where the superheroes had their "first appearances"

const firstAppearance = superheroes.map(hero => hero.first_appearance);
console.log("4. First Appearance:", firstAppearance)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



// 5. Create an array of all DC Comics superheroes. Did that work?
//    Then repeat the above function and also create an array with all Marvel Comics superheroes

const DCComics = superheroes.filter(hero => hero.publisher == "DC Comics");
console.log("5. DC Comics:", DCComics)

const marvelComics = superheroes.filter(hero => hero.publisher == "Marvel Comics");
console.log("5.1 Marvel Comics:", marvelComics)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 6. Add up the weight of all DC Comics superheroes. Pay attention! Conditional to the rescue!
// The weight you see here, what data type is that? A number? Or a string?
// Oh yeah, and do all superheroes have weight?

const weightDCComics = DCComics.map(hero => hero.weight);
console.log("6. Weight DC Comics:", weightDCComics)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 7. Do the same with all Marvel Comics superheroes

const weightMarvelComics = marvelComics.map(hero => hero.weight);
console.log("7. Weight Marvel Comics", weightMarvelComics)


////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


// 8. Find the heaviest superhero!

const weightAllHeroes = superheroes.map(hero => {
    const weight = hero.weight !== "unknown" ? parseInt(hero.weight) : 0;
    hero.weight = weight;
    return hero

});

const heaviest = weightAllHeroes.reduce(
    (currentHeaviestHero, currentHero) => {
        if (currentHero.weight > currentHeaviestHero.weight) {
            return currentHero;
        } else {
            return currentHeaviestHero;
        }
    },
    weightAllHeroes[0]
);


console.log("The heaviest weight is: ", heaviest)