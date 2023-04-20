var spottedList = document.getElementById("spotted-animals-list");

// Part1
    
const buttons = document.getElementsByClassName("big-five-button");
for (var i=0; i<buttons.length; i++) {
    buttons[i].addEventListener('click', event => {
        console.log(event.target.innerHTML);
        var newSpotted = document.createElement("li")
        newSpotted.className = "spotted-animals-list-item"
        spottedList.appendChild(newSpotted)
        newSpotted.innerHTML = event.target.innerHTML
    });
}


// Part 2

const removeFirst = document.getElementById("remove-first-item-button");
removeFirst.addEventListener('click', event => {
    firstAnimal = spottedList.getElementsByTagName("li")[0];
    spottedList.removeChild(firstAnimal);    
    });


// Part 3

const removeAll = document.getElementById("remove-all-button");
removeAll.addEventListener('click', event => {
    animals = spottedList.getElementsByTagName("li");
    spottedList.innerHTML = ''
});
