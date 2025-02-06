number = int(input("Enter any number : "))

sum = 0
i = 2

while i<=number:
    sum = sum + i
    i = i+2

print(f"2 + 4 + 6 +....+ {number} = {sum}")