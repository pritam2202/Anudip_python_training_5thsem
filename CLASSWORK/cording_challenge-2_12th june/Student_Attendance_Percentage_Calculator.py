# Attendance tuple (P = Present, A = Absent)
attendance = ('P','P','A','P','P','P','A','A','P','P','P','P','A','P','P')

# Count present days
present = attendance.count('P')

# Count absent days
absent = attendance.count('A')

# Calculate percentage
percent = (present / len(attendance)) * 100

# Print results
print(present)
print(absent)
print(round(percent, 2))

# Attendance status
if percent < 75:
    print("Below 75%")
else:
    print("Above 75%")