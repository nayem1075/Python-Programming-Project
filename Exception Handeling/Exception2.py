
#If number is 0 then have a exception

try :
     num1 = int(input("Enter any number : "))
     result = 20 / num1
     print(result)
except ZeroDivisionError :
    print("Dividing by zero is not possible")
