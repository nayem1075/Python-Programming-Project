
Words = 0
Letters = 0
Digits = 0

text = input("Enter any String : ")#My name is 123

for x in text:
    x = x.lower()

    if x>='a' and x<='z':
        Letters = Letters + 1

    elif x>='0' and x<='9':
        Digits = Digits + 1
    elif x==' ':
        Words = Words + 1

print("Number of letters : ",Letters)
print("Number of Digits : ",Digits)
print("Number of Words : ",Words)