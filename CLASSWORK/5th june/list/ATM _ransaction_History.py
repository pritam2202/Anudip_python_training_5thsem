transactions = [5000, -2000, 3000, -1000, -500, 7000]

# 1. Calculate the current balance
balance = 0
for t in transactions:
    balance += t

print("Current Balance:", balance)

# 2. Count total deposits and withdrawals
deposit_count = 0
withdrawal_count = 0

for t in transactions:
    if t > 0:
        deposit_count += 1
    elif t < 0:
        withdrawal_count += 1

print("Total Deposits:", deposit_count)
print("Total Withdrawals:", withdrawal_count)

# 3. Find the largest deposit and largest withdrawal
largest_deposit = None
largest_withdrawal = None

for t in transactions:
    if t > 0:
        if largest_deposit is None or t > largest_deposit:
            largest_deposit = t
    elif t < 0:
        if largest_withdrawal is None or t < largest_withdrawal:
            largest_withdrawal = t

print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)

# 4. Create separate lists for deposits and withdrawals
deposits = []
withdrawals = []

for t in transactions:
    if t > 0:
        deposits.append(t)
    elif t < 0:
        withdrawals.append(t)

print("Deposits List:", deposits)
print("Withdrawals List:", withdrawals)