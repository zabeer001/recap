const takeOrder = (customer, callback) => {
    console.log(`take order from ${customer}`);
    callback(customer);
}

const processOrder = (customer, callback) => {
    setTimeout(() => {
        console.log("processing order for customer 1");
        callback(customer);
    }, 3000); // Delay for 3 seconds
};

const deliveredOrder = (customer) => {
    console.log(`${customer} is delivered`);
};

//others function

takeOrder('zabeer', (customer) => {
    processOrder(customer, (customer) => {
        deliveredOrder(customer);
    })
})
console.log('hello');




