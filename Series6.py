number = int(input("Enter any number : "))
result = 1
i=1
while i<=number:
    result = result * i
    i = i+1
print(f"1 * 2 * 3 * ....* {number} = {result}")