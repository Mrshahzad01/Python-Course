# Example 01

class Student:
    def __init__(self, name, age, class_name, roll_number):
        self.name = name
        self.age = age
        self.class_name = class_name
        self.roll_number = roll_number


student_01 = Student("Ali", 20, "1st year", 101)
student_02 = Student("Ahmad", 19, "1st year", 102)
print("Student_01 Details:", student_01.name, student_01.age, student_01.class_name, student_01.roll_number)
print("Student-02 Details:")
print("Name:", student_02.name, "\n" "Age:", student_02.age, "\n" "Class:", student_02.class_name, "\n" "Roll Number:", student_02.roll_number)