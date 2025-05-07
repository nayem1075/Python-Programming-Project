
#xxargs it's work kind of dictionaries
def student(name,id) :
    print(name,id)
student(name = "Nayem",id = 24070151)

def students(**details) :
    print(details)
students(name = "Nayem Uddin",id = 101)

def number(**numbers) :
    print(numbers["second"])

number(first = 10,second = 30, third = 50)