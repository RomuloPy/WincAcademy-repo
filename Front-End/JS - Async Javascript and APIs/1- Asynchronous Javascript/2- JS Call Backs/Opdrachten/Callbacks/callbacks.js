function makeHomework(course, callback) {
    setTimeout(() => {
        console.log(`Okay, ok, I'm going to do my ${course} homework now!`);
        callback();
    }, 1000)
}


function doneWithHomework() {
    console.log("Look, Mom/Dad, I'm done with my homework!")
}


makeHomework("Math", doneWithHomework)