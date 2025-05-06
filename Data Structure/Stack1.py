
books = []
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop() # Remove Learn Java
print(books)
print("Now the top book is : ",books[-1])

books.pop() # Remove Learn C++
print(books)
print("Now the top book is : ",books[-1])

books.pop()
if not books :
    print("No Books left")