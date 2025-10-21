# Author: Bernard Kobina Forson Essel

#Base Class: Student
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade  # Private attribute using encapsulation

    # Getter method for grade
    def get_grade(self):
        return self.__grade

    # Setter method for grade
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade! Please enter a value between 0 and 100.")

    # Method to display student info
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.__grade}")

# Derived Class: GraduateStudent (Inherits from Student)
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        # Call parent class constructor
        super().__init__(name, age, grade)
        self.degree = degree

    # Overriding the display_info() method (Polymorphism)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.get_grade()}")  # Access private attribute through getter
        print(f"Degree Program: {self.degree}")

# Create objects (instances)
student1 = Student("Ama Mensah", 20, 88)
student2 = Student("Kwame Boateng", 19, 75)
grad_student = GraduateStudent("Bernard Essel", 24, 92, "MSc Telecommunications Engineering")

# Display their details
print("=== STUDENT DETAILS ===")
student1.display_info()
print("\n---")
student2.display_info()
print("\n---")
grad_student.display_info()

#Demonstrate encapsulation using getter and setter
print("\n=== UPDATING GRADES ===")
print(f"Old Grade for {student1.name}: {student1.get_grade()}")
student1.set_grade(95)
print(f"Updated Grade for {student1.name}: {student1.get_grade()}")
