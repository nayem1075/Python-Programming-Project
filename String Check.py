
text = input("Enter any text : ")

Words = 0
Digits = 0
Letters = 0
SpecialCharacter = 0

for i in text :
    i = i.upper()

    if i>='A' and i<='Z':
        Letters = Letters + 1
    elif i>='0' and i<='9':
        Digits = Digits + 1
    elif i== ' ':
        Words = Words + 1
    else:
        SpecialCharacter = SpecialCharacter + 1

print ("Number of Letters : ",Letters)
print("Number of Digits : ",Digits)
print("Number of Words : ",Words)
print("Number of Special Character : ",SpecialCharacter)
