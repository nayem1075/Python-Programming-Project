books = []

books.append("Learn Python")
books.append("Learn SQL")
books.append("Learn BASH")
print(books)

books.pop()
print("Now the top book is : ", books[-1])

books.pop()
print("Now the top book is : ",books[-1])

books.pop()

if not books :
    print("No books Left")
