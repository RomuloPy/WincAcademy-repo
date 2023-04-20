import camelcase from "camelcase";
import camelcaseKeys from "camelcase-keys";

const mystring = "--..fooBAR"
console.log(camelcase(mystring))

const person = {
    first_name: "rómulo",
    last_name: "Santos",
    phone_number: 628310522,
}

const camelcasePerson = camelcaseKeys(person);
console.log(camelcasePerson);

