# Student marks data
marks = {
    "Anuj": 92,
    "Rahul": 76,
    "Priya": 88,
    "Neha": 64,
    "Amit": 58,
    "Sneha": 95,
    "Karan": 81,
    "Pooja": 73,
    "Rohit": 47,
    "Anjali": 90
}

# 1. Display students scoring above 85 marks
print("Students Scoring Above 85:")
for student, score in marks.items():
    if score > 85:
        print(student)

# 2. Find the topper
topper = max(marks, key=marks.get)
print("\nTopper:")
print(f"{topper} ({marks[topper]})")

# 3. Find the student with the lowest marks
lowest = min(marks, key=marks.get)
print("\nLowest Scorer:")
print(f"{lowest} ({marks[lowest]})")

# 4. Calculate class average marks
average = sum(marks.values()) / len(marks)
print("\nAverage Marks:", round(average, 1))

# 5. Generate grades
print("\nGrades:")
grades = {}

for student, score in marks.items():
    if score >= 90:
        grades[student] = "A"
    elif score >= 75:
        grades[student] = "B"
    elif score >= 50:
        grades[student] = "C"
    else:
        grades[student] = "F"

for student, grade in grades.items():
    print(f"{student}: {grade}")

# 6. Create a list of scholarship students (marks ≥ 90)
scholarship_students = [student for student, score in marks.items() if score >= 90]

print("\nScholarship Students:")
print(scholarship_students)
