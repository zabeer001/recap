// return new Promise((resolve, reject) => {
//     // Do something asynchronously (e.g., make a network request)
    
//     if (/* operation is successful */) {
//         resolve(value); // Resolve the promise with a value when successful
//     } else {
//         reject(error); // Reject the promise with an error when something goes wrong
//     }
// });

const takeOrder = (customer) => {
    return new Promise((resolve) => {
        console.log(`take order from ${customer}`);
        resolve(customer);
    });
};

const processOrder = (customer) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`processing order for ${customer}`);
            resolve(customer);
        }, 3000); // Delay for 3 seconds
    });
};

const deliveredOrder = (customer) => {
    console.log(`${customer} is delivered`);
};

// Using Promises

takeOrder('zabeer')
    .then(processOrder)
    .then(deliveredOrder)
    .catch((error) => console.error(error));

console.log('hello');
