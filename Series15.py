#1 * 2 * 3 * ......*n
number = int(input("Enter the last number : "))

multiplication = 1

for i in range(1,number+1,1):
    multiplication = multiplication * i
print("1 X 2 x 3 X .... X",number," = ",multiplication)