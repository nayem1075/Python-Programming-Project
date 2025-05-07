
def largeNumber(a,b) :
    if a>b :
        return a
    else :
        return b

result = largeNumber(20,10)
print("Result : ",result)

#Use this function like a variable
maximum = largeNumber
print(maximum(10,30))