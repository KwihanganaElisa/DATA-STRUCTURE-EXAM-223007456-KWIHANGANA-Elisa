#Usage Selection Sort to sort the online learning platform for professional courses data based on priority.
class Course:
    def __init__(self, course_name, priority):
        self.course_name = course_name
        self.priority = priority

    def __str__(self):
        return f"Course: {self.course_name}, Priority: {self.priority}"

class OnlineLearningPlatform:
    def __init__(self):
        self.courses = []

    def add_course(self, course_name, priority):
        new_course = Course(course_name, priority)
        self.courses.append(new_course)
        print(f"Course '{course_name}' with priority {priority} added successfully!")
        print()

    def selection_sort(self):
        n = len(self.courses)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.courses[j].priority < self.courses[min_index].priority:
                    min_index = j
            self.courses[i], self.courses[min_index] = self.courses[min_index], self.courses[i]

    def display_courses(self):
        for course in self.courses:
            print(course)

# Execution
platform = OnlineLearningPlatform()

platform.add_course("Python Programming for Beginners", 3)
platform.add_course("Data Science Essentials", 1)
platform.add_course("Web Development with Django", 2)
platform.add_course("Machine Learning Basics", 4)

print("Courses before sorting:")
platform.display_courses()
print("----------------")

platform.selection_sort()

print("Courses after sorting based on priority:")
platform.display_courses()
