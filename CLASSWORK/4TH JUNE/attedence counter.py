total_student=30
present=0
absent=0
for i in range(1, total_student + 1):
  status=input(f"Student {i} is present or absent (p/a): ")

if status == "p":
        present += 1
else:
        absent += 1

print("Total Present:", present)
print("Total Absent:", absent)
