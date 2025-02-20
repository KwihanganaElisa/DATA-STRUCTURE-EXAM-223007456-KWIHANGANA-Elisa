#include <iostream>

using namespace std;

int main() {
    int num;

    // Ask the user to enter a number
    cout << "Enter a number: ";
    cin >> num;

    // Check if the number is even or odd
    if (num % 2 == 0) {
        cout << num << " is an even number." << endl;
    } else {
        cout << num << " is an odd number." << endl;
    }

    return 0;
}

