# Student ID Management System
# Basic Python Project

students = []


# Add a new student
def add_student():
    print("\n--- Add Student ---")

    sid = input("Enter Student ID: ")

    # Checking if the ID already exists
    for s in students:
        if s["id"] == sid:
            print("This Student ID already exists.")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    course = input("Enter Course: ")
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    student = {
        "id": sid,
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "branch": branch,
        "year": year,
        "phone": phone,
        "email": email,
        "attendance": 0,
        "marks": 0,
        "fees": "Not Paid"
    }

    students.append(student)

    print("Student added successfully!")


# Show all students
def show_students():
    print("\n--- Student List ---")

    if len(students) == 0:
        print("No student records available.")
        return

    for s in students:
        print("\nStudent ID:", s["id"])
        print("Name:", s["name"])
        print("Course:", s["course"])
        print("Branch:", s["branch"])
        print("Year:", s["year"])
        print("Phone:", s["phone"])
        print("------------------------")


# Search student using ID
def search_student():
    print("\n--- Search Student ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            print("\nStudent Found!")
            print("ID:", s["id"])
            print("Name:", s["name"])
            print("Age:", s["age"])
            print("Gender:", s["gender"])
            print("Course:", s["course"])
            print("Branch:", s["branch"])
            print("Year:", s["year"])
            print("Phone:", s["phone"])
            print("Email:", s["email"])
            print("Attendance:", s["attendance"], "%")
            print("Marks:", s["marks"], "%")
            print("Fees:", s["fees"])
            return

    print("Student not found.")


# Update student information
def update_student():
    print("\n--- Update Student ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            print("Enter the new details.")

            s["name"] = input("Name: ")
            s["age"] = input("Age: ")
            s["gender"] = input("Gender: ")
            s["course"] = input("Course: ")
            s["branch"] = input("Branch: ")
            s["year"] = input("Year: ")
            s["phone"] = input("Phone: ")
            s["email"] = input("Email: ")

            print("Student details updated.")
            return

    print("Student not found.")


# Delete a student
def delete_student():
    print("\n--- Delete Student ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            print("Student record deleted.")
            return

    print("Student not found.")


# Display ID card
def show_id_card():
    print("\n--- Student ID Card ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            print("\n")
            print("================================")
            print("         COLLEGE ID CARD")
            print("================================")
            print("Student ID :", s["id"])
            print("Name       :", s["name"])
            print("Course     :", s["course"])
            print("Branch     :", s["branch"])
            print("Year       :", s["year"])
            print("Phone      :", s["phone"])
            print("================================")

            return

    print("Student not found.")


# Update attendance
def attendance():
    print("\n--- Update Attendance ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            value = float(input("Enter attendance percentage: "))

            if value >= 0 and value <= 100:
                s["attendance"] = value
                print("Attendance updated.")
            else:
                print("Please enter a value between 0 and 100.")

            return

    print("Student not found.")


# Enter marks
def enter_marks():
    print("\n--- Enter Marks ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            value = float(input("Enter marks percentage: "))

            if value >= 0 and value <= 100:
                s["marks"] = value
                print("Marks added successfully.")
            else:
                print("Invalid marks.")

            return

    print("Student not found.")


# Show grade
def show_grade():
    print("\n--- Student Grade ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            marks = s["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            elif marks >= 40:
                grade = "E"
            else:
                grade = "F"

            print("Name:", s["name"])
            print("Marks:", marks, "%")
            print("Grade:", grade)

            return

    print("Student not found.")


# Change fee status
def fee_status():
    print("\n--- Fee Status ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            print("1. Paid")
            print("2. Not Paid")

            choice = input("Enter choice: ")

            if choice == "1":
                s["fees"] = "Paid"
                print("Fee status updated.")

            elif choice == "2":
                s["fees"] = "Not Paid"
                print("Fee status updated.")

            else:
                print("Invalid choice.")

            return

    print("Student not found.")


# Show complete student report
def student_report():
    print("\n--- Student Report ---")

    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:

            marks = s["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            elif marks >= 40:
                grade = "E"
            else:
                grade = "F"

            print("\nStudent Report")
            print("-------------------------")
            print("Student ID:", s["id"])
            print("Name:", s["name"])
            print("Course:", s["course"])
            print("Branch:", s["branch"])
            print("Year:", s["year"])
            print("Attendance:", s["attendance"], "%")
            print("Marks:", s["marks"], "%")
            print("Grade:", grade)
            print("Fees:", s["fees"])
            print("-------------------------")

            return

    print("Student not found.")


# Main program
while True:

    print("\n================================")
    print("     STUDENT ID MANAGEMENT")
    print("================================")

    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Student ID Card")
    print("7. Update Attendance")
    print("8. Enter Marks")
    print("9. Show Grade")
    print("10. Fee Status")
    print("11. Student Report")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        show_id_card()

    elif choice == "7":
        attendance()

    elif choice == "8":
        enter_marks()

    elif choice == "9":
        show_grade()

    elif choice == "10":
        fee_status()

    elif choice == "11":
        student_report()

    elif choice == "12":
        print("\nThank you for using the Student ID Management System!")
        break

    else:
        print("Invalid choice. Please try again.")