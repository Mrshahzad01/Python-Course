    # Create student class takes that takens name & marks of subjects as arguments in constructor. 
    # Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.mark = marks

    def average(self):
        if len(self.mark) == 0:
            print(f"{self.name} has no marks recorded.")
            return 
        
        total_mark = sum(self.mark)
        average = total_mark / len(self.mark)

        print(f"Student: {self.name}")
        print("Average mark:", average)


student1 = Student("Ali" ,[45,67,89,58])
student1.average()

