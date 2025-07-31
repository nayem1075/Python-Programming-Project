cars = ['bmw','audi','toyota','subaru']

print(cars) # Original list
print(sorted(cars)) #Sorting temporarily
print(cars) # Again Original list
cars.reverse()
print(cars)
print("Length of the list is : ",len(cars))


cars.sort()
print("Ascending order : ",cars)

cars.sort(reverse = True)
print("Desceding order : ",cars)

