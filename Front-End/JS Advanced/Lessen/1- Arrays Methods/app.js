// ARRAYS METHODS WITH !!!NO MUTATION!!!

const items = [
    { name: 'Bike',         price: 100 },
    { name: 'TV',           price: 200 },
    { name: 'Album',        price: 10 },
    { name: 'Book',         price: 5 },
    { name: 'Phone',        price: 500 },
    { name: 'Computer',     price: 1000 },
    { name: 'Keyboard',     price: 25 }
]

// .filter ARRAY METHOD - 

const filteredItems = items.filter((item) => {
    return item.price <= 100
})

console.log(items)
console.log(filteredItems)

////////////////////////////////////////////////////////////////

// .map ARRAY METHOD

const itemNames = items.map((item) => {
    return item.name
})

console.log(itemNames)

const itemPrices = items.map((item) => {
    return item.price
})

console.log(itemPrices)

///////////////////////////////////////////////////////////////

// .find ARRAY METHOD

const foundItem = items.find((item) => {
    return item.name === 'Book'
})

console.log(foundItem)

///////////////////////////////////////////////////////////////

// .forEach ARRAY METHOD

items.forEach((item) => {
    console.log(item.name)
})

///////////////////////////////////////////////////////////////

// .some ARRAY METHOD

const hasInexpensiveItems = items.some((item) => {
    return item.price <= 100
})

console.log(hasInexpensiveItems)



///////////////////////////////////////////////////////////////

// .every ARRAY METHOD

const hasInexpensiveItems1 = items.every((item) => {
    return item.price <= 1000
})

console.log(hasInexpensiveItems1)



///////////////////////////////////////////////////////////////

// .reduce ARRAY METHOD

const total = items.reduce((currentTotal, item) => {
    return item.price + currentTotal
}, 0)

console.log(total)


///////////////////////////////////////////////////////////////

// .includes ARRAY METHOD

const items1 = [1, 2, 3, 4, 5]

const includesTwo = items1.includes(2)

console.log(includesTwo)