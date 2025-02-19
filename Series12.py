number = int(input("Eter the last number : "))

sum = 0

for i in range(2,number+1,2):
    sum = sum + i*i
print("2^2 + 4^2 + 6^2 + .... ",number,"^2 = ",sum)