number = int(input("Enter any number : "))

first = 0
second = 1

i = 0
while i<number:
    print(first, end = " ")#for not print new line
    Fibonacci = first + second
    first = second
    second = Fibonacci
    i = i+1