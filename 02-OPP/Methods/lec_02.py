#        Static Methods 


"""Static methods are methods that don't use the self parameter(work at class level). 
They are defined using the @staticmethod decorator and can be called on the class itself without creating an instance."""



# class student:
#     @staticmethod
#     def college_name():   # Static Method
#         return "PGC"
    
# # Calling static method without creating an instance
# print(f"College name is {student.college_name()}")



#  Example with instance method and static method

class Student:  # Class Student
    def __init__(self, name, marks):    # Constructor method  
        self.name = name        # Object attribute for name
        self.marks = marks

    def wellcome(self):   # Instance Method
        print(f"Welcome {self.name} to the class!")

    @staticmethod
    def college_name():   # Static Method
        return "PGC"
    
# Creating an instance of the Student class
student1 = Student("Awais", 85)
student1.wellcome()  # Calling instance method wellcome
print(f"College name is {Student.college_name()}")  # Calling static method college_name