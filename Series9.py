
number = int(input("Enter the last number : "))

sum = 0

for i in range(1,number+1,2):
    sum = sum + i
print("1 + 3 + 5 + .... + ",number," = ",sum)