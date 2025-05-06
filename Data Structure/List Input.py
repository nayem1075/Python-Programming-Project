
n = input("Enter a text of numbers : ")
# 10 20 30 40
#split use for make list based on space
list = n.split() #10,20,30,40
sum = 0

for num in list:
    sum = sum + int (num)

print("Sum = ",sum)