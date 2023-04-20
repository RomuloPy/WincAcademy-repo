let toggleFlexStatus = false;

let toggleFlex = function() {
    let getFlex = document.querySelector(".flexbox");
    
    if (toggleFlexStatus === false) {
        getFlex.style.visibility = "visible";
        toggleFlexStatus = true;
    }

    else if (toggleFlexStatus === true) {
        getFlex.style.visibility = "hidden";

        toggleFlexStatus = false;
    }
}

// Home button (Change background to lightgrey)
let toggleHomeStatus = false;

let toggleHome = function () {
    let getHome = document.querySelector(".home");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleHomeStatus === false) {
        backgroundBody.style.background = "lightgrey";
        getFlex.style.visibility = "hidden";    
        toggleHomeStatus = true;
    }
}

// Red button (Change background to red)
let toggleRedStatus = false;

let toggleRed = function () {
    let getRed = document.querySelector(".red");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleRedStatus === false) {
        backgroundBody.style.background = "red";
        getFlex.style.visibility = "hidden";    
        toggleRedStatus = true;
    }
}

// Orange button (Change background to orange)
let toggleOrangeStatus = false;

let toggleOrange = function () {
    let getOrange = document.querySelector(".orange");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleOrangeStatus === false) {
        backgroundBody.style.background = "orange";
        getFlex.style.visibility = "hidden";    
        toggleOrangeStatus = true;
    }
}

// Purple button (Change background to purple)
let togglePurpleStatus = false;

let togglePurple = function () {
    let getPurple = document.querySelector(".purple");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (togglePurpleStatus === false) {
        backgroundBody.style.background = "purple";
        getFlex.style.visibility = "hidden";    
        togglePurpleStatus = true;
    }
}

// Green button (Change background to green)
let toggleGreenStatus = false;

let toggleGreen = function () {
    let getGreen = document.querySelector(".green");
    let backgroundBody = document.querySelector("body");
    let getFlex = document.querySelector(".flexbox");

    if (toggleGreenStatus === false) {
        backgroundBody.style.background = "green";
        getFlex.style.visibility = "hidden";    
        toggleGreenStatus = true;
    }
}
