print("════════════════════════════════════")
print("       🎓 STUDENT DATABASE MANAGER   ")
print("════════════════════════════════════")

students = []  # Empty list to store students

while True:
    print("\nChoose an option:")
    print(" [1] ➕ Add Student")
    print(" [2] 📋 View All Students")
    print(" [3] 🔍 Search Student by Name")
    print(" [4] 🚪 Exit")

    choice = input("\n➤ Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        age = input("Enter student age: ").strip()
        course = input("Enter student course: ").strip().title()

        # Store as tuple (name, age, course)
        student = (name, age, course)
        students.append(student)

        print(f"✅ Student {name} added successfully!")

    elif choice == "2":
        print("\n📋 All Students:")
        print("════════════════════════════════════")
        if len(students) == 0:
            print("⚠ No students found.")
        else:
            for i, student in enumerate(students, start=1):
                print(f"{i}. Name: {student[0]}, Age: {student[1]}, Course: {student[2]}")
        print("════════════════════════════════════")

    elif choice == "3":
        search_name = input("Enter name to search: ").strip().title()
        found = False
        for student in students:
            if student[0] == search_name:
                print(f"🔍 Found: Name: {student[0]}, Age: {student[1]}, Course: {student[2]}")
                found = True
                break
        if not found:
            print(f"⚠ Student {search_name} not found.")

    elif choice == "4":
        print("\n👋 Exiting Student Database Manager...")
        break

    else:
        print("⚠ Invalid choice. Try again.")
