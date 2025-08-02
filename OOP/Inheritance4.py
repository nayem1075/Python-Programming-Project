class A:
    def display(self):
        print("I am inside A class")

class B :
    def display(self):
        print("I am inside B class")

#If we pass then it's print those display() method then print whic one we inherit first (A,B) or (B,A)
class C (A,B) :
    pass
    #If we print display method then print C display method
    """
    def display(self):
        print("I am inside C class")
    """

object = C()
object.display()