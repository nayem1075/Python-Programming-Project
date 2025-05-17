
read = open("students.txt","r")

text = read.read()
print(text)

#Print file size
size = len(text)
print("File size : ",size)

read.close()