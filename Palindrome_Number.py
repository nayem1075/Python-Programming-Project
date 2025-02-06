number = int(input("Enter any number : "))

sum = 0
temp = number
while temp!=0:
    reminder = temp%10
    sum = sum*10 + reminder
    temp = temp//10
if number==sum:
    print(f"{number} is a Palindrome number")
else :
    print(f"{number} is not a Palindrome number")