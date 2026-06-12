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

# 1. Orange Cap winner (highest scorer)
orange_cap = max(runs, key=runs.get)

# 2. Lowest scorer
lowest_scorer = min(runs, key=runs.get)

# 3. Total runs scored
total_runs = sum(runs.values())

# 4. Players scoring more than 500 runs
above_500 = [player for player, score in runs.items() if score > 500]

# 5. Players scoring below 400 runs
below_400 = [player for player, score in runs.items() if score < 400]

# Display results
print("Orange Cap Winner:")
print(f"{orange_cap} ({runs[orange_cap]} runs)\n")

print("Lowest Scorer:")
print(f"{lowest_scorer} ({runs[lowest_scorer]} runs)\n")

print("Total Runs:", total_runs, "\n")

print("Players Scoring Above 500:")
for player in above_500:
    print(player)

print("\nPlayers Scoring Below 400:")
print(below_400)
