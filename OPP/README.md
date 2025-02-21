EXAMPLE ONE 
#include <iostream>  This includes a library that allows us to use cout (to print messages).
using namespace std; – This makes writing simpler (otherwise, we’d have to type std::cout).
Intmain() – Every C++ program must have a main() function—this is where the program starts.
 cout << "Hello, World!"; – This prints "Hello, World!" to the screen.
return 0; – This ends the program successfully.

EXAMPLE 2
int → Data type: This specifies the type of data the variable will hold. In this case, int stands for an integer, which means the variable can store whole numbers (both positive and negative) without decimals.
age → Variable name: This is the identifier or name of the variable. In this case, the variable is named age. You can use this name to reference and manipulate the value stored in the variable throughout your program.
25 → Value stored in the variable: This is the initial value that is assigned to the variable age at the time of its declaration. The value 25 is an integer, and it is stored in the variable age when this statement is executed.

EXAMPLE 3:
int: Used for whole numbers (e.g., 30).
float: Used for decimal numbers with single precision (e.g., 3.14).
double: Used for decimal numbers with double precision, offering more accuracy than float (e.g., 3.1415926535).
char: Used for a single character (e.g., 'A').
bool: Used for boolean values, true or false (e.g., true).
string: Used for sequences of characters (e.g., "Alice"), requires including <string> header.
EXAMPELE 4
1#include <iostream>:
This line tells the compiler to include the iostream library, which is used for input and output operations (like printing to the screen using cout).
using namespace std;:
This line makes all the names in the standard library available without needing to prefix them with std::. For example, you can use cout instead of std::cout and string instead of std::string.
. int main():
This is the main function where the program begins execution. Every C++ program must have a main() function, which serves as the entry point for the program.
int before main() indicates that the function returns an integer value (often used to signal the status of the program).
Variable Declarations and Initializations:
int age = 20;:
This line declares an integer variable named age and initializes it with the value 20.
double price = 19.99;:
This declares a double variable named price, which can store decimal values, and initializes it with the value 19.99.
char grade = 'A';:
This declares a char (character) variable named grade and initializes it with the value 'A', which is a single character.
string name = "Alice";:
This declares a string variable named name and initializes it with the string "Alice". Strings in C++ are sequences of characters enclosed in double quotes.
cout Statements (Output):
cout << "Name: " << name << endl;:
This line prints the text Name: , followed by the value stored in the variable name (which is "Alice"), and then moves to the next line using endl.
cout << "Age: " << age << endl;:
This prints Age: followed by the value of age (which is 20), then moves to a new line.
cout << "Price: $" << price << endl;:
This prints Price: $, followed by the value of price (which is 19.99), and then moves to the next line.
cout << "Grade: " << grade << endl;:
This prints Grade: followed by the value of grade (which is 'A'), and then moves to the next line.
                           return 0;
This is the return statement for the main() function. It returns the value 0, which typically indicates that the program has executed successfully.

EXAMPLE 5
This C++ program prompts the user to input their name and age. It uses cin to get user input and stores the values in the name and age variables. Then, it displays a personalized message using cout, showing the user's name and age. The program ends with return 0.
 
EXAMPLE 6
Variable Initialization: The integers a and b are initialized with values 10 and 3, respectively.
Sum: The program calculates and prints the sum of   a and b using the + operator.
Difference: It calculates and prints the difference between and b using the - operator.
Product, Quotient, and Remainder: The program calculates and prints the product (*), quotient (/), and remainder (%) of a and b.


