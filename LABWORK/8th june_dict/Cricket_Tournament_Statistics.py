# Dictionary storing runs scored by players
runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}

# Display players scoring more than 500 runs
print("Players Scoring More Than 500 Runs:")
for player, run in runs.items():
    if run > 500:
        print(player)

# Find highest and lowest scorer
orange_cap = max(runs, key=runs.get)
lowest = min(runs, key=runs.get)

print("\nOrange Cap Winner:", orange_cap, f"({runs[orange_cap]})")
print("Lowest Scorer:", lowest, f"({runs[lowest]})")

# Calculate total runs
print("\nTotal Tournament Runs:", sum(runs.values()))

# Create list of players scoring below 400
below_400 = [player for player, run in runs.items() if run < 400]
print("\nPlayers Scoring Below 400:")
print(below_400)

# Count players scoring between 400 and 600 runs
count = sum(1 for run in runs.values() if 400 <= run <= 600)
print("\nPlayers Between 400 and 600 Runs:", count)
