import java.util.Scanner;

public class SimpleCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Taking two numbers as input
        System.out.print("Enter first number: ");
        double num1 = scanner.nextDouble();

        System.out.print("Enter second number: ");
        double num2 = scanner.nextDouble();

        // Choosing the operation
        System.out.print("Choose an operation (+, -, *, /): ");
        char operator = scanner.next().charAt(0);

        double result;

        // Calculating based on chosen operation
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 != 0) {
                    result = num1 / num2;
                } else {
                    System.out.println("Error! Division by zero is not allowed.");
                    scanner.close();
                    return;
                }
                break;
            default:
                System.out.println("Invalid operator! Please choose +, -, *, or /.");
                scanner.close();
                return;
        }

        // Displaying the result
        System.out.println("The result is: " + result);
        scanner.close();
    }
}
