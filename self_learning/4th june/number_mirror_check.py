num = input("Enter a number: ")

length = len(num)

if length % 2 != 0:
    print("Not a Mirror Number")
else:
    half = length // 2

    if num[:half] == num[half:]:
        print("Mirror Number")
    else:
        print("Not a Mirror Number")