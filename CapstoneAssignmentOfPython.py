#Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display1(self):
        print(self.name)
        print(self.age)

# Derived class Student
class Student(Person):
    def __init__(self, course, name, age):
        self.course = course

        Person.__init__(self, name, age)

# Derived class Exam
class Exam(Student):
    def __init__(self, marks, course, name, age):
        self.marks = marks
        self.total = 0

        Student.__init__(self, course, name, age)

#Computing total marks
    def compute_total(self):
        for i in self.marks:
            self.total = sum(self.marks)

#Display of complete details
    def display_details(self):
        self.compute_total()
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}, Marks of three subjects: {self.marks}, Total computation: {self.total}")

#Instance of class Exam
obj =Exam([98, 99, 97], "BCA(AI & DS)", "Rohit", 18)

#method call of class Exam using object
obj.display_details()