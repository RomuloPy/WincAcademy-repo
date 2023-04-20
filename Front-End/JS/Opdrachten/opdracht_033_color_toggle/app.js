// Menu open/close
let toggleFlexStatus = false;

let toggleFlex = function () {
    let getFlex = document.querySelector(".flexbox");

    if (toggleFlexStatus === false) {
        getFlex.style.left = "0";
    }

    else if (toggleFlexStatus === false) {
        getFlex.style.left = "-350px";
    }
}
let menuButtonOpen = document.querySelector(".btn");
menuButtonOpen.addEventListener('mouseenter', toggleFlex);


// Home button (Change background to lightgrey)
let toggleHomeStatus = false;

let toggleHome = function () {
    let getHome = document.querySelector(".home");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");
    let getColorName = document.querySelector("#activeColorName");

    if (toggleHomeStatus === false) {
        backgroundBody.style.background = "lightgrey";
        document.getElementById("activeColorName").textContent = "Light Grey";
        getFlex.style.left = "-350px";
    }
}
let homeButton = document.querySelector(".home");
homeButton.addEventListener('click', toggleHome);


// Red button (Change background to red)
let toggleRedStatus = false;

let toggleRed = function () {
    let getRed = document.querySelector(".red");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleRedStatus === false) {
        backgroundBody.style.background = "red";
        document.getElementById("activeColorName").textContent = "Red";
        getFlex.style.left = "-350px";
    }
}
let redButton = document.querySelector(".red");
redButton.addEventListener('click', toggleRed);


// Orange button (Change background to orange)
let toggleOrangeStatus = false;

let toggleOrange = function () {
    let getOrange = document.querySelector(".orange");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleOrangeStatus === false) {
        backgroundBody.style.background = "orange";
        document.getElementById("activeColorName").textContent = "Orange";
        getFlex.style.left = "-350px";
    }
}
let orangeButton = document.querySelector(".orange");
orangeButton.addEventListener('click', toggleOrange);

// Purple button (Change background to purple)
let togglePurpleStatus = false;

let togglePurple = function () {
    let getPurple = document.querySelector(".purple");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (togglePurpleStatus === false) {
        backgroundBody.style.background = "purple";
        document.getElementById("activeColorName").textContent = "Purple";
        getFlex.style.left = "-350px";
    }
}
let purpleButton = document.querySelector(".purple");
purpleButton.addEventListener('click', togglePurple);

// Green button (Change background to green)
let toggleGreenStatus = false;

let toggleGreen = function () {
    let getGreen = document.querySelector(".green");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleGreenStatus === false) {
        backgroundBody.style.background = "green";
        document.getElementById("activeColorName").textContent = "Green";
        getFlex.style.left = "-350px";
    }
}
let greenButton = document.querySelector(".green");
greenButton.addEventListener('click', toggleGreen);


// Choose color with the keyboard
// 1- Grey, 2- Red, 3- Orange, 4- Purple, 5- Green
let checkKeyPress = function (key) {
    if (key.keyCode == "49") {
        toggleHome();
    }
    else if (key.keyCode == "50") {
        toggleRed();
    }
    else if (key.keyCode == "51") {
        toggleOrange();
    }
    else if (key.keyCode == "52") {
        togglePurple();
    }
    else if (key.keyCode == "53") {
        toggleGreen();
    }
}
window.addEventListener("keydown", checkKeyPress);


// Radio Buttons

let radioBtns = document.querySelectorAll("input[name='color']");

let findSelected = function () {
    let selected = document.querySelector("input[name='color']:checked");
}
radioBtns.forEach(radioBtn => {
    radioBtn.addEventListener("change", findSelected);
});