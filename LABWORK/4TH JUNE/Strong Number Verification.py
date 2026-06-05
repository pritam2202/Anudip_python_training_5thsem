num = int(input("Enter a number: "))

temp = num
sum_fact = 0

while temp > 0:
    digit = temp % 10

    factorial = 1
    for i in range(1, digit + 1):
        factorial *= i

    sum_fact += factorial
    temp //= 10

if sum_fact == num:
    print(num, "is a Strong Number")
else:
    print(num, "is not a Strong Number")
