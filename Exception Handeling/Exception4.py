
try :
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    result = num1 / num2
    print(result)
except ValueError :
    print("You have to insert only integer")
except ZeroDivisionError :
    print("Dividing by zero is not possible")
finally :
    print("Thanks")