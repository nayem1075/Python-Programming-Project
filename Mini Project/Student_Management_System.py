import os

file = "students_info.txt"

info = {}

if os.path.exists(file):
    with open(file, "r") as s:
        for line in s:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 3:
                print(f"Skipping invalid line: {line}")
                continue
            name, roll, grade = parts
            info[name] = (roll, grade)




def save_students_info():
    with open(file,"w") as s:
        for name,(roll,grade) in info.items():
            s.write(f"{name},{roll},{grade}\n")


while True:

    print("1. Add Student")
    print("2. View All Student")
    print("3. Search Student by Roll Number")
    print("4. Delete Student by Roll Number")
    print("5. Update Student Information")
    print("6. Exit")

    try :
        choice = int(input("Enter your choice : "))
    except ValueError:
        print("Invalid choice.Please enter a valid choice.")

    if choice ==1:
        name = input("Enter Student Name : ")
        roll = input("Enter Roll Number : ")
        grade = input("Enter Grade : ")
        info[name] = (roll,grade)
        print(f"{name} added successfully.")
        save_students_info()

    elif choice ==2:
        if info:
             print("\nAll Student Information")
             for name,(roll,grade) in info.items():
                  print(f"{name} : {roll},{grade}")
        else :
            print("No Students Found")

    elif choice ==3:
        roll = input("Enter roll number : ")
        found = False
        for name, (r, g) in info.items():
            if r == roll:
                print(f"{name} : {r},{g}")
                found = True
                break
        if not found:
            print("No Information found")


    elif choice ==4:
        roll = input("Enter Roll Number : ")
        found = False
        for name in list(info):
            if info[name][0] == roll:
                del info[name]
                save_students_info()
                print(f"{name} removed successfully.")
                found = True
                break
        if not found :
            print("Roll Number not found.")

    elif choice == 5:

        roll = input("Enter Roll Number to Update : ")
        found = False
        for name in list(info):

            if info[name][0] == roll:
                new_name = input("Enter new Student Name : ")
                new_roll = input("Enter new Roll Number : ")
                new_grade = input("Enter new Grade : ")
                del info[name]
                info[new_name] = (new_roll, new_grade)
                save_students_info()
                print(f"{new_name} updated successfully.")
                found = True
                break
        if not found:
            print("Roll number not found.")

    elif choice ==6:
        print("Exit The program")
        break

    else:
        print("Invalid Choice.Please enter a valid choice.")





