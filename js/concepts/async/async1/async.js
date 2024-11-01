const processOrder = (customer) => {
    console.log("processing order for customer 1");

    // Simulate delay (3000ms) using while loop
    const delay = 3000;
    const startTime = new Date().getTime();
    while (new Date().getTime() - startTime < delay) {
        // Busy wait - this will block the event loop
    }
    console.log('hello');
    
}

console.log('take order from customer 1');
processOrder();
console.log('completed order for customer 1');




