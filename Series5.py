number = int(input("Enter any number : "))
sum = 0
i = 1
while i<=number:
    sum = sum + i*i
    i = i+1
print(f"1^2 + 2^2 + 3^2 + .....+ {number}^{number} = {sum}")