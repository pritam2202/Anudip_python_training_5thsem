#9. Warehouse Product Inspection
#Problem Statement
#Product IDs and quality status:
#products = [
# (101, "Pass"),
# (102, "Fail"),
# (103, "Pass"),
# (104, "Fail"),
# (105, "Pass")
#]
#Write a program to:
#• Display failed product IDs.
#• Count passed and failed products.
#• Calculate pass percentage.
#• Stop checking if 3 failures are found. 


products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

passed = 0
failed = 0

print("Failed Product IDs:")

for pid, status in products:
    if status == "Fail":
        print(pid)

for pid, status in products:
    if status == "Pass":
        passed += 1
    else:
        failed += 1

percentage = (passed / len(products)) * 100

print("Passed:", passed)
print("Failed:", failed)
print("Pass Percentage:", percentage)

fail_count = 0

for pid, status in products:
    if status == "Fail":
        fail_count += 1

    if fail_count == 3:
        print("3 Failures Found")
        break
