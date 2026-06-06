#Employee data is stored as tuples:
##employees = [
# ("Rahul", 35000),
# ("Priya", 55000),
# ("Amit", 42000),
# ("Neha", 65000)
#]
#Write a program to:
#• Display employees earning above ₹50,000.
#• Find the highest-paid employee.
#• Calculate total salary expenditure.
#• Count employees earning below ₹40,000. 


employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

highest = employees[0]
total = 0
count = 0

print("Employees earning above ₹50000:")

for name, salary in employees:
    if salary > 50000:
        print(name)

    if salary > highest[1]:
        highest = (name, salary)

    total += salary

    if salary < 40000:
        count += 1

print("Highest Paid Employee:", highest[0])
print("Total Salary Expenditure:", total)
print("Employees below ₹40000:", count)
