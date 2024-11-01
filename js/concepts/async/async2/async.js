const processOrder = (customer) => {
    setTimeout(() => {
        console.log("processing order for customer 1");
   
    }, 3000); // Delay for 3 seconds
};

console.log('take order from customer 1');
processOrder();
console.log("completed order for customer 1");



