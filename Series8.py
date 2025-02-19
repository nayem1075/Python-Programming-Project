
number = int(input("Enter the last number : "))

sum = 0

for i in range(2,number+1,2): 
    sum = sum + i
print("2 + 4 + 6 + ..... + ",number," = ",sum)
