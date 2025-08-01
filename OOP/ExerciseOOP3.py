class Vehicle():
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def showInfo(self):
        print("This is Vehicle method")

class Car(Vehicle) :
    def __init__(self,brand,year,num_doors):
        super().__init__(brand,year)
        self.num_doors = num_doors

    def showInfo(self):
        print("Brand : ",self.brand)
        print("Year : ",self.year)
        print("Number of doors : ",self.num_doors)

class Motorcycle(Vehicle) :
     def __init__(self,brand,year,has_sidecar) :
         super().__init__(brand,year)
         self.has_sidecar = has_sidecar

     def showInfo(self):
         print("Brand : ", self.brand)
         print("Year : ", self.year)
         print("Has sidecar : ", self.has_sidecar)


C = Car("Toyota",2020,4)
C.showInfo()

M = Motorcycle("Yamaha",2022,False)
M.showInfo()
