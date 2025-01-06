#Implementation of Stack and Array to manage data in the online learning platform for professional courses.
class OnlineLearningPlatform:
    def __init__(self):
        self.courses = []
        self.recent_courses = []

    def add_course(self, course_name):
        self.courses.append(course_name)
        print(f"Course '{course_name}' added to the platform.")
        print()

    def view_courses(self):
        print("Available Courses on the Platform:")
        for course in self.courses:
            print(course)
        print("-------------------")
    def enroll_in_course(self, course_name):
        if course_name in self.courses:
            self.recent_courses.append(course_name)
            print(f"Enrolled in '{course_name}'.")
        else:
            print(f"Course '{course_name}' not available on the platform.")
        print()

    def view_recent_course(self):
        if self.recent_courses:
            print(f"Most recently enrolled course: {self.recent_courses[-1]}")
            print("----------------")
        else:
            print("No recent courses to display.")

    def exit_course(self):
        if self.recent_courses:
            exited_course = self.recent_courses.pop() 
            print(f"Exited course '{exited_course}'.")
            
        else:
            print("No courses to exit.")
        print()

platform = OnlineLearningPlatform()

platform.add_course("Python Programming for Beginners")
platform.add_course("Data Science Essentials")
platform.add_course("Web Development with Django")


platform.view_courses()
platform.enroll_in_course("Python Programming for Beginners")
platform.enroll_in_course("Data Science Essentials")

platform.view_recent_course()
platform.exit_course()
platform.view_courses()
platform.view_recent_course()

