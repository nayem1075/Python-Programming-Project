n = int(input("Enter the number for pattern : "))
"""
    *
   **
  ***
 ****
*****

"""

for i in range (n+1):
    print(" "*(n-i)+"*"*i)