
num1 = {1,2,3,4,5,5}#Don't print duplicate value
num2 = set([4,5,6])

num2.add(7)
num1.remove(2)

print(num1)
print(num2)

#Check number
print (7 in num1)
print(7 in num2)
print(8 not in num1)