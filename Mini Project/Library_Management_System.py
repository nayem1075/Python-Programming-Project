import os

file = "books.txt"

books = {}

if os.path.exists(file):
    with open(file,"r") as f:
        for line in f:
            line = line.strip()
            if line and "," in line:
                name,author,publication_year = line.split(",",2)
                books[name] = author,publication_year

def save_books():
    with open(file, "w") as f:
        for name, (author, publication_year) in books.items():
            f.write(f"{name},{author},{publication_year}\n")


while True:

    print("____Library management Systeem____")
    print("1. Add Book")
    print("2. View all books")
    print("3. Search book")
    print("4. Delete Book")
    print("5. Update Book")
    print("6. Exit System")

    try :
        choice = int(input("Enter your choice : "))
    except ValueError :
        print("Please enter a valid choice like 1,2,3,4.....")
        continue

    if choice ==1:
        name = input("Enter book name : ")
        author = input("Enter author name : ")
        publication_year = input("Enter publication year of this book : ")
        books[name] = (author,publication_year)
        print(f"{name} added successfully")
        save_books()

    elif choice ==2:
        if books :
            print("All Books\n")
            for name,(author,publication_year) in books.items() :
                print(f"{name} : {author},{publication_year}")
        else:
            print("No books found.")

    elif choice ==3:
        name = input("Enter book name : ")
        if name in books :
            print(f"{name} : {books[name]}")

        else :
            print("Book not found")

    elif choice ==4:
        name = input("Enter book name : ")
        if name in books :
            del books[name]
            print(f"{name} deleted successfully.")
            save_books()
        else :
            print("Book not found.")

    elif choice ==5:
        old_name = input("Enter books name : ")
        if old_name in books :
            new_name = input("Enter new book name : ")
            author = input("Enter new author name : ")
            publication_year = input("Enter new published year : ")
            del books[old_name]
            books[new_name] = (author,publication_year)
            save_books()
            print(f"{old_name} updated successfully to {new_name}")

        else :
            print("No books found.")

    elif choice ==6:
        print("Exit library management system")
        break

    else :
        print("Invalid choice.Please enter a valid choice.")



