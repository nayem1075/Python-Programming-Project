
import os

file = "contacts.txt"

contacts = {}
if os.path.exists(file):
    with open(file,"r") as f:
        for line in f:
            line = line.strip()
            if line and "," in line:
                name, phone_number = line.split(",", 1)
                contacts[name] = phone_number

def save_contacts():
    with open(file,"w") as f:
        for name,phone_number in contacts.items():
            f.write(f"{name},{phone_number}\n")

while True :
    print("______Contact Book_____")
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Delete Contact")
    print("4.Search Contacts")
    print("5.Exit")

    try:
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        name = input("Enter your name : ")
        phone_number = input("Enter your phone number : ")
        contacts[name] = phone_number
        print(f"{name} added successfully")
        save_contacts()

    elif choice == 2:
        if contacts:
            print("All Accounts.")
            for name, phone_number in contacts.items():
                print(f"{name} : {phone_number}")
        else:
            print("No contacts found.")


    elif choice == 3:
        name = input("Enter your name : ")

        if name in contacts:
            del contacts[name]
            print(f"{name} removed successfully")
            save_contacts()
        else :
            print("Contact not found.")


    elif choice == 4:
        name = input("Enter your name : ")
        if name in contacts:
            print(f"{name} : {contacts[name]}")
        else:
            print("Contact not found.")


    elif choice==5:
        print("Exiting contact book.")
        break
    else :
        print("Invalid choice.Please try again.")



