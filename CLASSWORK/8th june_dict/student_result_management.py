student_marks = {
    "Anuj": 85,
    "Rahul": 72,
    "Priya": 91,
    "Neha": 68,
    "Amit": 78
}

# Display marks of Priya
print("Priya's marks:", student_marks["Priya"])

# Display marks of Amit
print("Amit's marks:", student_marks["Amit"])

# Update Rahul's marks
student_marks["Rahul"] = 80
print("Updated Rahul's marks:", student_marks["Rahul"])

# Check whether Rohan exists
if "Rohan" in student_marks:
    print("Rohan exists in the records.")
else:
    print("Rohan does not exist in the records.")

# Display all student names
print("Student Names:", list(student_marks.keys()))

# Display all marks
print("Marks:", list(student_marks.values()))

# Find the highest scorer
highest_scorer = max(student_marks, key=student_marks.get)
print("Highest Scorer:", highest_scorer, "-", student_marks[highest_scorer])

# Add new student Rohan
student_marks["Rohan"] = 88

# Remove Neha
del student_marks["Neha"]

# Display all student records
print("Final Student Records:")
for name, marks in student_marks.items():
    print(name, ":", marks)
