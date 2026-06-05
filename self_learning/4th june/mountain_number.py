num = input("Enter a number: ")

peak_found = False
is_mountain = True

for i in range(1, len(num)):
    if not peak_found:
        if num[i] > num[i - 1]:
            continue
        elif num[i] < num[i - 1]:
            peak_found = True
        else:
            is_mountain = False
            break
    else:
        if num[i] < num[i - 1]:
            continue
        else:
            is_mountain = False
            break

# Must have both increasing and decreasing parts
if not peak_found:
    is_mountain = False

if is_mountain:
    print("Mountain Number")
else:
    print("Not a Mountain Number")