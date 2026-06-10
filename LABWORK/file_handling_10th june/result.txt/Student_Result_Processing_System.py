# Student Result Processing System

# Load student data
def load_students():
    students = []
    with open("results.txt", "r") as file:
        for line in file:
            sid, name, marks = line.strip().split(",")
            students.append([sid, name, int(marks)])
    return students


# Assign grade
def grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 40:
        return "C"
    else:
        return "F"


# Display students
def display(students):
    for s in students:
        print(s)


# Search student
def search(students):
    sid = input("Enter ID: ")
    for s in students:
        if s[0] == sid:
            print(s)
            return
    print("Not Found")


# Generate grade file
def generate(students):
    with open("grades.txt", "w") as file:
        for s in students:
            file.write(f"{s[0]},{s[1]},{s[2]},{grade(s[2])}\n")
    print("grades.txt created")


while True:
    students = load_students()

    print("\n1.Display 2.Search 3.Top/Low 4.Avg 5.Pass/Fail 6.Grades 7.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        display(students)

    elif ch == 2:
        search(students)

    elif ch == 3:
        print("Top:", max(students, key=lambda x: x[2]))
        print("Low:", min(students, key=lambda x: x[2]))

    elif ch == 4:
        print("Avg:", sum(s[2] for s in students) / len(students))

    elif ch == 5:
        pass_count = len([s for s in students if s[2] >= 40])
        fail_count = len(students) - pass_count
        print("Pass:", pass_count, "Fail:", fail_count)

    elif ch == 6:
        generate(students)

    elif ch == 7:
        break
