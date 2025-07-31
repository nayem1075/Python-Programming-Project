class Student :
    name = ""
    roll = ""

    def set_Value(self,name,roll):
            self.name = name
            self.roll = roll

    def display(self):
         print(f"Name : {self.name},Roll : {self.roll}")

S1 = Student()
S1.set_Value("Nayem",101)
S1.display()

S2 = Student()
S2.set_Value("Rahim",102)
S2.display()