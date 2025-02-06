number = int(input("Enter any number : "))
sum = 0
temp = number

while temp!=0:
    reminder = temp%10
    sum = sum+reminder
    temp = temp//10#/ is float but // is integer
print(f"Sum of {number} = {sum}")
