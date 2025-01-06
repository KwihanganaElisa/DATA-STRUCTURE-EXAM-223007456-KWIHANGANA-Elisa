class TreeNode:
    def __init__(self, course_name):
        self.course_name = course_name
        self.sub_courses = []

    def add_sub_course(self, sub_course):
        self.sub_courses.append(sub_course)

    def display(self, level=0):
        print("  " * level + f"Course: {self.course_name}")
        for sub_course in self.sub_courses:
            sub_course.display(level + 1)

class CourseTree:
    def __init__(self):
        self.root = None

    def set_root(self, course_name):
        self.root = TreeNode(course_name)

    def add_sub_course(self, parent_course_name, sub_course_name):
        parent_course = self._find_course(self.root, parent_course_name)
        if parent_course:
            sub_course = TreeNode(sub_course_name)
            parent_course.add_sub_course(sub_course)
            print(f"Sub-course '{sub_course_name}' added to '{parent_course_name}' successfully!")
        else:
            print(f"Course '{parent_course_name}' not found.")

    def _find_course(self, node, course_name):
        if not node:
            return None
        if node.course_name == course_name:
            return node
        for sub_course in node.sub_courses:
            found = self._find_course(sub_course, course_name)
            if found:
                return found
        return None

    def display_courses(self):
        if self.root:
            print("Courses and Sub-courses Hierarchy:")
            self.root.display()
            print("----------------")
        else:
            print("No courses available.")

# execution
course_tree = CourseTree()

course_tree.set_root("Professional Courses")

course_tree.add_sub_course("Professional Courses", "Python Programming")
course_tree.add_sub_course("Professional Courses", "Data Science Essentials")
course_tree.add_sub_course("Python Programming", "Basic Python")
course_tree.add_sub_course("Python Programming", "Advanced Python")
course_tree.add_sub_course("Data Science Essentials", "Data Analysis with Python")
course_tree.add_sub_course("Data Science Essentials", "Machine Learning Basics")

course_tree.display_courses()
