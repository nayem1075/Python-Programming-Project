
file = open("students.txt","r")

#print(file.readable())

"""
#Read File
text = file.read()
print(text)

#Check file size
size = len(text)
print("File size : ",size)

"""
#File print together in list
list1 = file.readlines()
print(list1)

file.close()