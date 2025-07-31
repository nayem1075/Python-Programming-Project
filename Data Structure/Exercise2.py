
name = ['Nayem','Faisal','Akib']
print(name[0])
print(name[1])
print(name[2])
print(f"First name of the list is {name[0]}")

name[1] = 'Jubair'
print(name)

name.append('Ainan')
print(name)

name.insert(1,'Arif')
print(name)

del name[1]
print(name)

name.pop()
print(name)

name.pop(1)
print(name)

name.remove('Akib')
print(name)