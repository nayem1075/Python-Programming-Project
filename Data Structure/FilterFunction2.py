
def even(x):
    return x%2==0

number = [1,2,3,4,5]

result = list(filter(even,number))
print(result)