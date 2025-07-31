class Student :
    roll = ""
    gpa = ""

    def __init__ (self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll},GPA : {self.gpa}")

s1 = Student(101,3.85)
s1.display()

s2 = Student(102,3.75)
s2.display()