number = int(input("Enter the last number : "))

sum = 0

for i in range(1,number+1,1):
    sum = sum + 1/i
print("1 + 1/2 + 1/3 + .... + 1/",number," = ",sum)
