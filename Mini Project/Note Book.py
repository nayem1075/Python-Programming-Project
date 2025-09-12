
import os

note = "notes.txt"

notes = {}

if os.path.exists(note):
    with open(note,"r") as n:
        for line in n:
            line = line.strip()
            if line and "," in line:
                topic,text = line.split(",",1)
                notes[topic] = text

def save_notes():
    with open(note,"w") as n:
        for topic,text in notes.items():
            n.write(f"{topic},{text}\n")

while True:

    print("_____Note Book_____")
    print("1. Add Note")
    print("2. View Note")
    print("3. Delete Note")
    print("4. Search note")
    print("5. Exit")

    try :
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid choice. please try again")
        continue

    if choice ==1:
        topic = input("Enter topic name for add note : ")
        text = input("Enter text about your topic : ")
        notes[topic]= text
        print(f"{topic} added successfully")
        save_notes()

    elif choice==2:
        if notes :
            print("All Notes")
            for topic,text in notes.items():
                print(f"{topic} : {text}")
        else:
            print("No notes found")

    elif choice==3:
        topic = input("Enter topic name for delete : ")
        if topic in notes :
            del notes[topic]
            print(f"{topic} deleted successfully")
            save_notes()
        else:
            print("No notes found to delete")


    elif choice ==4:
        topic = input("Enter topic name for search : ")
        if topic in notes :
            print(f"{topic} : {notes[topic]}")
        else:
            print("No notes found")

    elif choice ==5:
        print("Exit note books.")
        break

    else:
        print("Invalid choice. please try again.")






