#include <iostream>

using namespace std;

int main() {
    // Declare an array of 5 integers
    int numbers[5] = {10, 20, 30, 40, 50};

    // Use a for loop to print all the numbers
    cout << "The numbers in the array are: " << endl;
    for (int i = 0; i < 5; i++) {
        cout << numbers[i] << " ";
    }

    cout << endl; // Move to the next line

    return 0;
}

