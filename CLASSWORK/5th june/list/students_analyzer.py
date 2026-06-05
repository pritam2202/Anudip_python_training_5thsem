<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate the current balance
balance = 0
for t in transactions:
    balance += t

print("Current Balance:", balance)

# 2. Count total deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

for t in transactions:
    if t > 0:
        deposit_count += 1
    elif t < 0:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# 3. Find the largest deposit and largest withdrawal
largest_deposit = None
largest_withdrawal = None

for t in transactions:
    if t > 0:
        if largest_deposit is None or t > largest_deposit:
            largest_deposit = t
    elif t < 0:
        if largest_withdrawal is None or t < largest_withdrawal:
            largest_withdrawal = t

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# 4. Create separate lists for deposits and withdrawals
deposits = []
withdrawals = []

for t in transactions:
    if t > 0:
        deposits.append(t)
    elif t < 0:
        withdrawals.append(t)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)
=======
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
#A teacher has marks of students stored in a list. marks = [78, 45, 92, 35, 88, 40, 99, 56]

# 1. Display all passed students (marks >= 40)
passed_students = []
for mark in marks:
    if mark >= 40:
        passed_students.append(mark)

print("Passed Students:", passed_students)

# 2. Count the number of failed students
failed_count = 0
for mark in marks:
    if mark < 40:
        failed_count += 1

print("Number of Failed Students:", failed_count)

# 3. Find the highest and lowest marks without using max() or min()
highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# 4. Create a new list containing marks above 75
above_75 = []
for mark in marks:
    if mark > 75:
        above_75.append(mark)

print("Marks Above 75:", above_75)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
=======
>>>>>>> 59736abfa11bf98f465f7bb17b97766de850eff4
