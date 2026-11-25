#STUDENT MANAGEMENT SYSTEM
students = {}

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Average Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        students[sid] = [name, marks]

        print("Student Added Successfully!")

    # View Students
    elif choice == "2":

        if students == {}:
            print("No Student Found")

        else:
            for sid, data in students.items():
                print("ID:", sid)
                print("Name:", data[0])
                print("Marks:", data[1])

    # Search Student
    elif choice == "3":

        sid = input("Enter Student ID: ")

        if sid in students:
            print("Name:", students[sid][0])
            print("Marks:", students[sid][1])

        else:
            print("Student Not Found")

    # Delete Student
    elif choice == "4":

        sid = input("Enter Student ID: ")

        if sid in students:
            del students[sid]
            print("Student Deleted Successfully!")

        else:
            print("Student Not Found")

    # Average Marks
    elif choice == "5":

        if students == {}:
            print("No Student Records")

        else:
            total = 0

            for data in students.values():
                total = total + data[1]

            average = total / len(students)

            print("Average Marks:", average)

    # Exit
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice!")