# Employee ID Validation and Analysis System

# Input Employee ID
emp_id = input("Enter Employee ID: ")

# 1. Count uppercase letters
uppercase_count = 0

# 2. Count digits
digit_count = 0

# List to store digits
digit_list = []

# Sum of digits
digit_sum = 0

# Traverse each character
for ch in emp_id:
    if ch.isupper():
        uppercase_count += 1

    if ch.isdigit():
        digit_count += 1
        digit_list.append(int(ch))
        digit_sum += int(ch)

# 3. Extract joining year
joining_year = emp_id[3:7]

# 4. Extract employee name
employee_name = emp_id[7:-3]

# 5. Validate ID
valid = True

# Check if starts with EMP
if not emp_id.startswith("EMP"):
    valid = False

# Check year contains exactly 4 digits
if len(joining_year) != 4 or not joining_year.isdigit():
    valid = False

# Check last 3 characters are digits
if len(emp_id) < 10 or not emp_id[-3:].isdigit():
    valid = False

# Display Results
print("\nEmployee ID:", emp_id)

print("\nUppercase Letters:", uppercase_count)
print("Digits:", digit_count)

print("\nJoining Year:", joining_year)
print("Employee Name:", employee_name)

print("\nDigit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("\nID Status: Valid")
else:
    print("\nID Status: Invalid")
