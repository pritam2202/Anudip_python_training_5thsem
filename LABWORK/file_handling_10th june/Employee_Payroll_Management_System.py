# Employee Payroll Management System using File Handling

# Load employee data from file
def load_employees():
    employees = []
    with open("employees.txt", "r") as file:
        for line in file:
            emp_id, name, salary = line.strip().split(",")
            employees.append([emp_id, name, int(salary)])
    return employees


# Add new employee to file
def add_employee():
    with open("employees.txt", "a") as file:
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")
        file.write(f"\n{emp_id},{name},{salary}")
    print("Employee Added Successfully")


# Display all employees
def display(employees):
    print("\nEmployee Records:")
    for e in employees:
        print(e)


# Search employee by ID
def search(employees):
    eid = input("Enter Employee ID: ")
    for e in employees:
        if e[0] == eid:
            print("Found:", e)
            return
    print("Not Found")


# Calculate average salary
def average(employees):
    total = sum(e[2] for e in employees)
    print("Average Salary:", total / len(employees))


# Highest and lowest salary
def high_low(employees):
    print("Highest:", max(employees, key=lambda x: x[2]))
    print("Lowest:", min(employees, key=lambda x: x[2]))


# Salary categories
def categories(employees):
    for e in employees:
        if e[2] >= 60000:
            print(e[1], "High")
        elif e[2] >= 40000:
            print(e[1], "Medium")
        else:
            print(e[1], "Low")


# Menu-driven program
while True:
    employees = load_employees()

    print("\n1.Display 2.Search 3.Avg 4.High/Low 5.Above 50K 6.Add 7.Category 8.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        display(employees)

    elif choice == 2:
        search(employees)

    elif choice == 3:
        average(employees)

    elif choice == 4:
        high_low(employees)

    elif choice == 5:
        for e in employees:
            if e[2] > 50000:
                print(e)

    elif choice == 6:
        add_employee()

    elif choice == 7:
        categories(employees)

    elif choice == 8:
        break
