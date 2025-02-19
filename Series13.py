number = int(input("Enter the last number : "))

sum = 0

for i in range(1,number+1,2):
    sum = sum + i*i
print("1^2 + 3^2 + 5^2 + .... ",number,"^2 = ",sum)