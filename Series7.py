# 1+2+3+4+.....+n

number = int(input("Enter the last number : "))

sum = 0
#Here in range between 3 parameter (Staring number, Ending number+1 for <= number, increement)
for i in range(1,number+1,1):
    sum = sum + i
print("1 + 2 + 3 + .... +",number," = ",sum)
