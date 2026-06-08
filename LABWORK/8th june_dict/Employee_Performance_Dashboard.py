# Dictionary storing employee performance scores
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}

# Display employees scoring above 80
print("Employees Scoring Above 80:")
for emp, score in performance.items():
    if score > 80:
        print(emp)

# Find top performer
top = max(performance, key=performance.get)
print("\nTop Performer:", top, f"({performance[top]})")

# Count employees needing improvement
improvement = sum(1 for score in performance.values() if score < 60)
print("\nEmployees Needing Improvement:", improvement)

# Calculate average score
average = sum(performance.values()) / len(performance)
print("\nAverage Score:", round(average, 1))

# Categorize employees
excellent = [emp for emp, score in performance.items() if score >= 90]
good = [emp for emp, score in performance.items() if 75 <= score <= 89]
average_list = [emp for emp, score in performance.items() if 60 <= score <= 74]
poor = [emp for emp, score in performance.items() if score < 60]

print("\nExcellent:")
print(excellent)

print("\nGood:")
print(good)

print("\nAverage:")
print(average_list)

print("\nPoor:")
print(poor)
