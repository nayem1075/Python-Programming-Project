n = int(input("Enter the number for pattern : "))

"""
*        (2*i-1)
***
*****
*******
"""
for i in range(n+1):
    print((2*i-1)*"*")