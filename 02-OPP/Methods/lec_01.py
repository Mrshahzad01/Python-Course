#                                    Methods 
"""In Python, methods are functions that are defined within a class 
and are used to perform operations using the data contained in the class."""



#                  Full Explain code with comments

class Student:  # Class Student
    college = "PGC"  # Class attribute
    def __init__(self, name, marks):    # Constructor method  
        self.name = name        # Object attribute for name
        self.marks = marks

    def wellcome(self):   # Method 01
        print(f"Welcome {self.name} to the class!")

    def get_marks(self):   # Method 02  
        return self.marks
    
# Creating an instance of the Student class
student1 = Student("Awais", 85)
print(f"Student college is {Student.college}")   # Accessing class attribute
student1.wellcome()  # Calling method wellcome
print(f"your marks are {student1.get_marks()}")   # Calling method get_marks
