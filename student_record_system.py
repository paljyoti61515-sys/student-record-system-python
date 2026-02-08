import json

FILE_NAME = "students_data.json"

def load_students():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_students():
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)

students = load_students()

def add_student():
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students.append({"name": name, "marks": marks})
    save_students()
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s["name"], "-", s["marks"])

def search_student():
    name = input("Enter name to search: ")
    for s in students:
        if s["name"].lower() == name.lower():
            print("Found:", s["name"], "-", s["marks"])
            return
    print("Student not found")

def update_student():
    name = input("Enter name to update marks: ")
    for s in students:
        if s["name"].lower() == name.lower():
            new_marks = int(input("Enter new marks: "))
            s["marks"] = new_marks
            save_students()
            print("Marks updated successfully!")
            return
    print("Student not found")

def delete_student():
    name = input("Enter name to delete: ")
    for s in students:
        if s["name"].lower() == name.lower():
            students.remove(s)
            save_students()
            print("Student deleted successfully!")
            return
    print("Student not found")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice")
