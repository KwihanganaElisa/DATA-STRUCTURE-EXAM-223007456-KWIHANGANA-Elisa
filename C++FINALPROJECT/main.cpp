#include <iostream>
#include <algorithm>
#include <cstring>

struct Student {
    char name[30];
    float* grades;
    int nGrades;
    
    Student() : grades(nullptr), nGrades(0) {}
    
    ~Student() {
        delete[] grades;
    }
};

// Abstract base class
class GradeMetric {
public:
    virtual float compute(const Student* student) = 0;
    virtual ~GradeMetric() = default;
};

// Mean metric implementation
class MeanMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        float sum = 0.0f;
        float* ptr = student->grades;
        for (int i = 0; i < student->nGrades; ++i) {
            sum += *(ptr + i);  // pointer arithmetic
        }
        return sum / student->nGrades;
    }
};

// Median metric implementation
class MedianMetric : public GradeMetric {
public:
    float compute(const Student* student) override {
        if (student->nGrades == 0) return 0.0f;
        
        // Create temporary array for sorting
        float* temp = new float[student->nGrades];
        float* ptr = student->grades;
        for (int i = 0; i < student->nGrades; ++i) {
            *(temp + i) = *(ptr + i);  // pointer arithmetic
        }
        
        std::sort(temp, temp + student->nGrades);
        
        float median;
        if (student->nGrades % 2 == 1) {
            median = *(temp + student->nGrades / 2);
        } else {
            median = (*(temp + student->nGrades / 2 - 1) + *(temp + student->nGrades / 2)) / 2.0f;
        }
        
        delete[] temp;
        return median;
    }
};

// Function to add grade
void addGrade(Student& student, float grade) {
    float* newGrades = new float[student.nGrades + 1];
    
    // Copy existing grades using pointer arithmetic
    for (int i = 0; i < student.nGrades; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }
    
    *(newGrades + student.nGrades) = grade;
    
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades++;
}

// Function to remove grade by index
void removeGrade(Student& student, int index) {
    if (index < 0 || index >= student.nGrades) {
        std::cout << "Invalid index!\n";
        return;
    }
    
    if (student.nGrades == 1) {
        delete[] student.grades;
        student.grades = nullptr;
        student.nGrades = 0;
        return;
    }
    
    float* newGrades = new float[student.nGrades - 1];
    
    // Copy grades before index
    for (int i = 0; i < index; ++i) {
        *(newGrades + i) = *(student.grades + i);
    }
    
    // Copy grades after index
    for (int i = index + 1; i < student.nGrades; ++i) {
        *(newGrades + i - 1) = *(student.grades + i);
    }
    
    delete[] student.grades;
    student.grades = newGrades;
    student.nGrades--;
}

void displayStudent(const Student& student) {
    std::cout << "Student: " << student.name << "\n";
    std::cout << "Grades: ";
    for (int i = 0; i < student.nGrades; ++i) {
        std::cout << *(student.grades + i) << " ";
    }
    std::cout << "\n";
}

int main() {
    Student student;
    
    // Dynamic array of metric pointers
    GradeMetric** metrics = new GradeMetric*[2];
    metrics[0] = new MeanMetric();
    metrics[1] = new MedianMetric();
    
    std::cout << "Student Grade Metrics Application\n";
    std::cout << "Enter student name: ";
    std::cin.getline(student.name, 30);
    
    int choice;
    do {
        std::cout << "\n1. Add Grade\n";
        std::cout << "2. Remove Grade\n";
        std::cout << "3. Display Grades\n";
        std::cout << "4. Calculate Metrics\n";
        std::cout << "5. Exit\n";
        std::cout << "Choice: ";
        std::cin >> choice;
        
        switch (choice) {
            case 1: {
                float grade;
                std::cout << "Enter grade: ";
                std::cin >> grade;
                addGrade(student, grade);
                std::cout << "Grade added!\n";
                break;
            }
            
            case 2: {
                if (student.nGrades == 0) {
                    std::cout << "No grades to remove!\n";
                    break;
                }
                displayStudent(student);
                int index;
                std::cout << "Enter index to remove (0-" << student.nGrades - 1 << "): ";
                std::cin >> index;
                removeGrade(student, index);
                std::cout << "Grade removed!\n";
                break;
            }
            
            case 3: {
                displayStudent(student);
                break;
            }
            
            case 4: {
                if (student.nGrades == 0) {
                    std::cout << "No grades available!\n";
                    break;
                }
                
                std::cout << "Mean: " << metrics[0]->compute(&student) << "\n";
                std::cout << "Median: " << metrics[1]->compute(&student) << "\n";
                break;
            }
            
            case 5:
                std::cout << "Goodbye!\n";
                break;
                
            default:
                std::cout << "Invalid choice!\n";
        }
    } while (choice != 5);
    
    // Cleanup
    delete metrics[0];
    delete metrics[1];
    delete[] metrics;
    
    return 0;
}
