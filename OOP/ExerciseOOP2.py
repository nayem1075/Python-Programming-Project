class Shape():
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2

    def area(self):
        print("It is Shape class")

class Triangle(Shape):
    #area
    def area(self):
        area = 0.5 * self.a1 * self.a2
        print(area)

class Rectangle(Shape):
    #area
    def area(self):
        area = self.a1 * self.a2
        print(area)

T = Triangle(10,20)
T.area()
R = Rectangle(5,10)
R.area()