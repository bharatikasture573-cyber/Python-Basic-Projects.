def student_database():
    students = {}
    while True:
        print("\n******* STUDENT DATABASE MENU *******")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                roll = int(input("Enter Roll Number: "))
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")
                students.update({
                    roll: 
                    {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })
                print("Student added successfully.")

            elif choice == 2:
                roll = int(input("Enter Roll Number to Search: "))
                student = students.get(roll)
                if student:
                    print("\nStudent Found")
                    print("Name:", student["Name"])
                    print("Age:", student["Age"])
                    print("City:", student["City"])
                else:
                    print("Student not found.")

            # Display All Students
            elif choice == 3:
                if len(students) == 0:
                    print("No student records found.")
                else:
                    print("\n******* Student Records *******")
                    for roll, details in students.items():
                        print("Roll No :", roll)
                        print("Name :", details["Name"])
                        print("Age :", details["Age"])
                        print("City :", details["City"])
                        print("--------------------------")
            elif choice == 4:
                print("Exiting Student Database...")
                break
            else:
                print("Invalid choice. Please enter 1 to 4.")

        except ValueError:
            print("Error: Please enter valid numeric input.")
student_database()