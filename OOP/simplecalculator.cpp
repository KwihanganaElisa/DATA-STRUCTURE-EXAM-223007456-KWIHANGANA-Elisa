#include <iostream>

using namespace std;

// Function for addition
double add(double a, double b) {
    return a + b;
}

// Function for subtraction
double subtract(double a, double b) {
    return a - b;
}

// Function for multiplication
double multiply(double a, double b) {
    return a * b;
}

// Function for division
double divide(double a, double b) {
    if (b == 0) {
        cout << "Error! Division by zero is not allowed." << endl;
        return 0;
    }
    return a / b;
}

int main() {
    int choice;
    double num1, num2, result;

    // Display menu
    cout << "Select an operation to perform:" << endl;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Division" << endl;
    cout << "Enter your choice (1-4): ";
    cin >> choice;

    // Take input for numbers
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    // Perform operation based on user choice
    switch (choice) {
        case 1:
            result = add(num1, num2);
            cout << "Result: " << result << endl;
            break;
        case 2:
            result = subtract(num1, num2);
            cout << "Result: " << result << endl;
            break;
        case 3:
            result = multiply(num1, num2);
            cout << "Result: " << result << endl;
            break;
        case 4:
            result = divide(num1, num2);
            cout << "Result: " << result << endl;
            break;
        default:
            cout << "Invalid choice! Please enter a number between 1 and 4." << endl;
    }

    return 0;
}

