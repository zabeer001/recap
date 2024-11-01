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

const processOrder2 = (customer) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`processing order 2 for ${customer}`);
            resolve(customer);
        }, 2000); // Delay for 2 seconds
    });
};

const processOrder3 = (customer) => {
    return new Promise((resolve) => {
        setTimeout(() => {
            console.log(`processing order 3 for ${customer}`);
            resolve(customer);
        }, 1000); // Delay for 1 second
    });
};

const deliveredOrder = (customer) => {
    console.log(`${customer} is delivered`);
};

const handleOrder = async () => {
    try {
        const customer = await takeOrder('zabeer');
        await processOrder(customer);
        await processOrder2(customer);
        await processOrder3(customer);
        deliveredOrder(customer);
    } catch (error) {
        console.error("An error occurred:", error);
    }
};

// Run the async function
handleOrder();

console.log(`hello`);
