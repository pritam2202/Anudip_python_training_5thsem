"""Create Attendance tracker of 30 students. Ask the user to input roll number of student and also 
input whether student is Present or Absent. Store the data in dictionary where roll number will 
be used as a key and Attendance as Value. 
Display the roll number of students who are Present"""
# Attendance Tracker using Dictionary

# Create an empty dictionary
attendance = {}

# Input attendance of 30 students
for i in range(30):
    roll_no = input("Enter Roll Number: ")
    status = input("Enter Attendance (Present/Absent): ")

    # Store roll number as key and attendance as value
    attendance[roll_no] = status

# Display roll numbers of students who are Present
print("\nRoll Numbers of Present Students:")

for roll_no, status in attendance.items():
    if status.lower() == "present":
        print(roll_no)