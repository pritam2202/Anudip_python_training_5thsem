# Employee records stored in a tuple
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)

# 1. Display details of employees scoring 80 or above
print("Employees scoring 80 or above:")
for emp in employees:
    if emp[2] >= 80:
        print(emp)

# 2. Count employees who need improvement (score below 60)
count_improvement = 0
for emp in employees:
    if emp[2] < 60:
        count_improvement += 1

print("\nNumber of employees needing improvement:", count_improvement)

# 3. Find the employee with the highest score
highest_emp = max(employees, key=lambda x: x[2])

print("\nEmployee with highest score:")
print("ID:", highest_emp[0])
print("Name:", highest_emp[1])
print("Score:", highest_emp[2])

# 4. Create a list of names scoring above 75
high_performers = [emp[1] for emp in employees if emp[2] > 75]

print("\nEmployees scoring above 75:")
print(high_performers)

# 5. Display performance category for each employee
print("\nPerformance Categories:")
for emp in employees:
    score = emp[2]

    if score >= 90:
        category = "Excellent"
    elif score >= 75:
        category = "Good"
    elif score >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"

    print(emp[1], ":", category)
