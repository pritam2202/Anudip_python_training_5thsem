above_50000 = 0
below_1000 = 0
total_amount = 0

while True:
    amount = float(input("Enter transaction amount (-1 to stop): "))

    if amount == -1:
        break

    total_amount += amount

    if amount > 50000:
        above_50000 += 1

    if amount < 1000:
        below_1000 += 1

print("\nTransactions above ₹50,000:", above_50000)
print("Transactions below ₹1,000:", below_1000)
print("Total transaction amount: ₹", total_amount)