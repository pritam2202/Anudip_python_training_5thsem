# Accept marks of 5 subjects

total = 0
failed = 0

for i in range(5):
    marks = int(input("Enter marks: "))
    total += marks

    if marks < 40:
        failed += 1

percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks =", total)
print("Percentage =", percentage)
print("Grade =", grade)
print("Failed Subjects =", failed)
