number = int(input("Enter the last number : "))

sum = 0

for i in range(4,number+1,4):
    sum = sum + i
print("4 + 8 + 12 + .... + ",number," = ",sum)