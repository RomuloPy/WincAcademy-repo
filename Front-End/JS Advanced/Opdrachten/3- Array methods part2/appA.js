const superheroes = [
    {name: "Batman", alter_ego: "Bruce Wayne"},
    {name: "Superman", alter_ego: "Clark Kent"},
    {name: "Spiderman", alter_ego: "Peter Parker"}]
    
const findSpiderMan = function(array) {
    spider = array.find(s => s.name === "Spiderman")
    return spider
}
    
console.log(findSpiderMan(superheroes))
    // Find Spiderman
    // result should be: {name: "Spiderman", alter_ego: "Peter Parker"}