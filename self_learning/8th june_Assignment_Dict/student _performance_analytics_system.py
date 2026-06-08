# ==========================================
# STUDENT PERFORMANCE ANALYTICS SYSTEM
# ==========================================

# Dictionary with 30 students
students = {
    "S101": {"name": "Anuj", "marks": 85},
    "S102": {"name": "Rahul", "marks": 72},
    "S103": {"name": "Aman", "marks": 91},
    "S104": {"name": "Neha", "marks": 66},
    "S105": {"name": "Riya", "marks": 48},
    "S106": {"name": "Karan", "marks": 77},
    "S107": {"name": "Simran", "marks": 95},
    "S108": {"name": "Amit", "marks": 52},
    "S109": {"name": "Pooja", "marks": 88},
    "S110": {"name": "Vikas", "marks": 34},
    "S111": {"name": "Rohit", "marks": 69},
    "S112": {"name": "Sneha", "marks": 81},
    "S113": {"name": "Deepak", "marks": 58},
    "S114": {"name": "Divya", "marks": 93},
    "S115": {"name": "Ajay", "marks": 40},
    "S116": {"name": "Yash", "marks": 75},
    "S117": {"name": "Komal", "marks": 61},
    "S118": {"name": "Ishita", "marks": 86},
    "S119": {"name": "Harsh", "marks": 97},
    "S120": {"name": "Tanya", "marks": 55},
    "S121": {"name": "Manish", "marks": 73},
    "S122": {"name": "Nitin", "marks": 89},
    "S123": {"name": "Aayush", "marks": 44},
    "S124": {"name": "Shreya", "marks": 79},
    "S125": {"name": "Kajal", "marks": 68},
    "S126": {"name": "Priya", "marks": 92},
    "S127": {"name": "Naman", "marks": 38},
    "S128": {"name": "Ritu", "marks": 83},
    "S129": {"name": "Sahil", "marks": 71},
    "S130": {"name": "Meena", "marks": 99}
}

# -----------------------------
# 1. Display all students
# -----------------------------
def display_students():
    print("\n--- Student Records ---")
    for sid in students:
        print(sid, students[sid])

# -----------------------------
# 2. Search student
# -----------------------------
def search_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Found:", students[sid])
    else:
        print("Student not found")

# -----------------------------
# 3. Add student
# -----------------------------
def add_student():
    sid = input("Enter new ID: ")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students[sid] = {"name": name, "marks": marks}
    print("Student added")

# -----------------------------
# 4. Update marks
# -----------------------------
def update_marks():
    sid = input("Enter ID to update: ")
    if sid in students:
        marks = int(input("Enter new marks: "))
        students[sid]["marks"] = marks
        print("Marks updated")
    else:
        print("Student not found")

# -----------------------------
# 5. Delete student
# -----------------------------
def delete_student():
    sid = input("Enter ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted")
    else:
        print("Student not found")

# -----------------------------
# 6. Topper & Lowest
# -----------------------------
def topper_lowest():
    top = low = None

    for sid in students:
        if top is None or students[sid]["marks"] > students[top]["marks"]:
            top = sid
        if low is None or students[sid]["marks"] < students[low]["marks"]:
            low = sid

    print("Topper:", top, students[top])
    print("Lowest:", low, students[low])

# -----------------------------
# 7. Class Average
# -----------------------------
def class_average():
    total = 0
    for sid in students:
        total += students[sid]["marks"]

    avg = total / len(students)
    print("Class Average:", avg)
    return avg

# -----------------------------
# 8. Pass / Fail count
# -----------------------------
def pass_fail():
    p = f = 0

    for sid in students:
        if students[sid]["marks"] >= 50:
            p += 1
        else:
            f += 1

    print("Pass:", p)
    print("Fail:", f)

# -----------------------------
# 9. Grades
# -----------------------------
def show_grades():
    print("\n--- Grades ---")
    for sid in students:
        m = students[sid]["marks"]

        if m >= 90:
            g = "A"
        elif m >= 75:
            g = "B"
        elif m >= 50:
            g = "C"
        else:
            g = "F"

        print(sid, students[sid]["name"], m, g)

# -----------------------------
# 10. Above average students
# -----------------------------
def above_average():
    avg = class_average()

    print("\nAbove Average Students:")
    for sid in students:
        if students[sid]["marks"] > avg:
            print(sid, students[sid])

# -----------------------------
# 11. Top 5 students (no sort)
# -----------------------------
def top5():
    temp = students.copy()

    print("\nTop 5 Students:")
    for _ in range(5):
        top = None
        for sid in temp:
            if top is None or temp[sid]["marks"] > temp[top]["marks"]:
                top = sid

        print(top, temp[top])
        del temp[top]

# -----------------------------
# 12. Scholarship students
# -----------------------------
def scholarship():
    print("\nScholarship Students (>85):")
    for sid in students:
        if students[sid]["marks"] > 85:
            print(sid, students[sid])

# =============================
# MENU SYSTEM
# =============================
while True:
    print("\n===== MENU =====")
    print("1. Display Students")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Topper & Lowest")
    print("7. Class Average")
    print("8. Pass/Fail Count")
    print("9. Grades")
    print("10. Above Average")
    print("11. Top 5 Students")
    print("12. Scholarship Students")
    print("13. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        display_students()
    elif choice == 2:
        search_student()
    elif choice == 3:
        add_student()
    elif choice == 4:
        update_marks()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        topper_lowest()
    elif choice == 7:
        class_average()
    elif choice == 8:
        pass_fail()
    elif choice == 9:
        show_grades()
    elif choice == 10:
        above_average()
    elif choice == 11:
        top5()
    elif choice == 12:
        scholarship()
    elif choice == 13:
        print("Exit")
        break
    else:
        print("Invalid choice")
