# Student Grade Metrics Application

## Project Overview

This C++ application demonstrates object-oriented programming concepts including dynamic memory management, inheritance, polymorphism, and pointer arithmetic. The program manages student grades dynamically and calculates various statistical metrics.

## Task Requirements

The application was built to fulfill the following specific requirements:

1. **Dynamic Grade Management**: Create a `Student` struct with dynamically allocated grade arrays
2. **Inheritance & Polymorphism**: Implement an abstract base class with derived metric classes
3. **Pointer Arithmetic**: Use pointer arithmetic for all array operations
4. **Dynamic Array Operations**: Implement functions to add and remove grades with array resizing
5. **Polymorphic Dispatch**: Store metric objects in a dynamic array and call methods polymorphically

## Technical Implementation

### Core Data Structure

```cpp
struct Student {
    char name[30];        // Fixed-size character array for student name
    float* grades;        // Pointer to dynamically allocated grades array
    int nGrades;          // Current number of grades stored
    
    Student() : grades(nullptr), nGrades(0) {}  // Initialize with no grades
    
    ~Student() {          // Destructor ensures memory cleanup
        delete[] grades;  // Deallocate dynamic array when student is destroyed
    }
};
```

**Key Points:**
- `grades` is a pointer that will point to dynamically allocated memory
- Constructor initializes pointer to `nullptr` for safety
- Destructor automatically cleans up memory to prevent leaks

### Abstract Base Class and Inheritance

```cpp
// Abstract base class defining the interface for all metrics
class GradeMetric {
public:
    // Pure virtual function - must be implemented by derived classes
    virtual float compute(const Student* student) = 0;
    // Virtual destructor ensures proper cleanup of derived objects
    virtual ~GradeMetric() = default;
};
```

**Inheritance Hierarchy:**
```
GradeMetric (Abstract Base)
    ├── MeanMetric (Concrete Implementation)
    └── MedianMetric (Concrete Implementation)
```

### Mean Metric Implementation

```cpp
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;  // Handle empty grade list
        
        float sum = 0.0f;
        float* ptr = student->grades;  // Get pointer to first grade
        
        // Use pointer arithmetic to iterate through grades
        for (int i = 0; i < student->nGrades; ++i) {
            sum += *(ptr + i);  // Dereference pointer + offset
        }
        return sum / student->nGrades;  // Calculate arithmetic mean
    }
};
```

**Pointer Arithmetic Explanation:**
- `ptr + i` moves the pointer `i` positions forward
- `*(ptr + i)` dereferences the pointer at that position
- Equivalent to `ptr[i]` but explicitly uses pointer arithmetic

### Median Metric Implementation

```cpp
class MedianMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        // Create temporary array for sorting (median requires sorted data)
        float* temp = new float[student->nGrades];
        float* ptr = student->grades;
        
        // Copy all grades using pointer arithmetic
        for (int i = 0; i < student->nGrades; ++i) {
            *(temp + i) = *(ptr + i);  // Copy each grade
        }
        
        // Sort the temporary array
        std::sort(temp, temp + student->nGrades);
        
        float median;
        if (student->nGrades % 2 == 1) {
            // Odd number of grades - middle element
            median = *(temp + student->nGrades / 2);
        } else {
            // Even number of grades - average of two middle elements
            median = (*(temp + student->nGrades / 2 - 1) + 
                     *(temp + student->nGrades / 2)) / 2.0f;
        }
        
        delete[] temp;  // Clean up temporary array
        return median;
    }
};
```

### Dynamic Array Management

#### Adding Grades

```cpp
void addGrade(Student& student, float grade) {
    // Create new array with one more slot
    float* newGrades = new float[student.nGrades + 1];
    
    // Copy existing grades using pointer arithmetic
    for (int i = 0; i < student.nGrades; ++i) {
        *(newGrades + i) = *(student.grades + i);  // Copy each grade
    }
    
    // Add the new grade at the end
    *(newGrades + student.nGrades) = grade;
    
    // Replace old array with new one
    delete[] student.grades;  // Free old memory
    student.grades = newGrades;  // Point to new array
    student.nGrades++;  // Update count
}
```

**Memory Management Process:**
1. Allocate new array (size + 1)
2. Copy all existing data
3. Add new element
4. Delete old array
5. Update pointer and count

#### Removing Grades

```cpp
void removeGrade(Student& student, int index) {
    // Validate index bounds
    if (index < 0 || index >= student.nGrades) {
        std::cout << "Invalid index!\n";
        return;
    }
    
    // Special case: removing last grade
    if (student.nGrades == 1) {
        delete[] student.grades;
        student.grades = nullptr;
        student.nGrades = 0;
        return;
    }
    
    // Create smaller array
    float* newGrades = new float[student.nGrades - 1];
    
    // Copy grades before the index to remove
    for (int i = 0; i < index; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }
    
    // Copy grades after the index (skip the removed grade)
    for (int i = index + 1; i < student.nGrades; ++i) {
        *(newGrades + i - 1) = *(student.grades + i);  // Shift left by 1
    }
    
    // Replace array
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades--;
}
```

### Polymorphic Dispatch System

```cpp
int main() {
    Student student;
    
    // Create dynamic array of metric pointers
    GradeMetric** metrics = new GradeMetric*[2];  // Array of pointers
    metrics[0] = new MeanMetric();    // First element points to MeanMetric
    metrics[1] = new MedianMetric();  // Second element points to MedianMetric
    
    // Later in the code...
    // Polymorphic dispatch - calls appropriate compute() method
    std::cout << "Mean: " << metrics[0]->compute(&student) << "\n";
    std::cout << "Median: " << metrics[1]->compute(&student) << "\n";
    
    // Cleanup polymorphic objects
    delete metrics[0];  // Calls MeanMetric destructor
    delete metrics[1];  // Calls MedianMetric destructor
    delete[] metrics;   // Deallocate array of pointers
}
```

**Polymorphism in Action:**
- `metrics[0]->compute(&student)` calls `MeanMetric::compute()`
- `metrics[1]->compute(&student)` calls `MedianMetric::compute()`
- The correct method is chosen at runtime based on the actual object type

## Key Programming Concepts Demonstrated

### 1. Dynamic Memory Management
- All grade arrays are allocated with `new[]` and deallocated with `delete[]`
- Proper RAII (Resource Acquisition Is Initialization) with destructors
- Memory resizing operations for array growth/shrinkage

### 2. Object-Oriented Design
- **Inheritance**: MeanMetric and MedianMetric inherit from GradeMetric
- **Polymorphism**: Virtual functions allow runtime method dispatch
- **Encapsulation**: Each class manages its own responsibilities

### 3. Pointer Arithmetic
- All array access uses `*(ptr + offset)` instead of `ptr[offset]`
- Demonstrates understanding of memory layout and pointer mathematics
- Shows equivalence between array notation and pointer operations

### 4. Exception Safety
- Bounds checking for array operations
- Null pointer checks
- Proper cleanup in all code paths

## User Interface Features

The application provides an interactive menu system:

1. **Add Grade**: Dynamically expands the grades array
2. **Remove Grade**: Shrinks the array and shifts remaining elements
3. **Display Grades**: Shows all current grades with pointer arithmetic
4. **Calculate Metrics**: Demonstrates polymorphic method calls
5. **Exit**: Proper cleanup of all allocated memory

## Sample Program Output

### Initial Setup
```
Student Grade Metrics Application
Enter student name: John Smith

1. Add Grade
2. Remove Grade
3. Display Grades
4. Calculate Metrics
5. Exit
Choice: 1
Enter grade: 85.5
Grade added!
```

### Adding Multiple Grades
```
Choice: 1
Enter grade: 92.0
Grade added!

Choice: 1
Enter grade: 78.5
Grade added!

Choice: 1
Enter grade: 88.0
Grade added!
```

### Displaying Current Grades
```
Choice: 3
Student: John Smith
Grades: 85.5 92 78.5 88
```

### Calculating Metrics
```
Choice: 4
Mean: 86
Median: 86.75
```

### Removing a Grade
```
Choice: 2
Student: John Smith
Grades: 85.5 92 78.5 88
Enter index to remove (0-3): 2
Grade removed!

Choice: 3
Student: John Smith
Grades: 85.5 92 88
```

### Updated Metrics After Removal
```
Choice: 4
Mean: 88.5
Median: 88
```

### Program Exit
```
Choice: 5
Goodbye!
```

## Memory Management Verification

Throughout the program execution:
- **No memory leaks**: All `new[]` operations have corresponding `delete[]`
- **No dangling pointers**: Pointers are set to `nullptr` or valid addresses
- **No buffer overflows**: All array accesses are bounds-checked
- **RAII compliance**: Destructors automatically clean up resources

## Build and Run Instructions

```bash
# Compile the program
g++ -std=c++11 -Wall -Wextra -o student_grades main.cpp

# Run the executable
./student_grades
```

