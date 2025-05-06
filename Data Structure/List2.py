
subjects = ["C","C++","Java","Python","BASIC","SQL"]

#Length of this list = 6, beacuse it's start with 1
print("Length of the list = ",len(subjects))

subjects.append("TOC")#For added another one in this list
print(subjects)

subjects.insert(2,"OS")#for added another one in list where we want
print(subjects)

subjects.remove("BASIC")#If we want to remove anyone of the list
print(subjects)

subjects = ["C","C++","Java","Python","BASIC","SQL"]
subjects.sort()#It means print the list using serial of (a to z)
print(subjects)

numbers = [20,10,4,100]
numbers.reverse()#For print last to first
print(numbers)

numbers = [20,10,4,100]
print(numbers)
numbers.pop()#For remove last numbers of the list
numbers.pop()#For remove last numbers of the list
print(numbers)

subjects1 = ["C","C++","Java","Python","BASIC","SQL"]
subjects2 = subjects1.copy()#Copy all elements of this list
print(subjects2)

numbers = [20,10,4,100]
position = numbers.index(100)#For find the index number
print(position)

numbers = [20,10,4,100,4]
Count = numbers.count(4)#For count anyone of this list, how many times it has
print(Count)