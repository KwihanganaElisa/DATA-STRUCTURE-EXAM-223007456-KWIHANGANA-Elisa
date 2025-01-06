# Implementation of Circular Queue for course processing in the online learning platform

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, course_name):
        if self.is_full():
            print("Queue is full! Cannot add more courses for processing.")
            return
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = course_name
        print(f"Course '{course_name}' added to the processing queue.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! No courses to process.")
            return None
        course = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"Course '{course}' processed and removed from the queue.")
        return course

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        print("Current courses in the processing queue:")
        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print("\n-------------------")


queue_size = 5
course_queue = CircularQueue(queue_size)

course_queue.enqueue("Python Programming")
course_queue.enqueue("Data Science Essentials")
course_queue.enqueue("Web Development with Django")
course_queue.enqueue("Machine Learning Basics")
course_queue.enqueue("Cybersecurity Fundamentals")

course_queue.enqueue("Cloud Computing 101")

course_queue.display()

course_queue.dequeue()
course_queue.dequeue()

course_queue.display()

course_queue.enqueue("Artificial Intelligence")
course_queue.enqueue("Blockchain Essentials")

course_queue.display()
