n = int(input("Enter number of elements: "))

count = 1
max_count = 1

prev = int(input("Enter number: "))

for i in range(n - 1):
    num = int(input("Enter number: "))
    
    if num > prev:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

    prev = num

print("Longest Sequence Length =", max_count)