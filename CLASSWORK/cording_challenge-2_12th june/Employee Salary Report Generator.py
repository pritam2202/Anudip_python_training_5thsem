# Employee performance data
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

# Employees scoring above 80
above_80 = [e for e, s in performance.items() if s > 80]

# Employees needing improvement
improve = sum(1 for s in performance.values() if s < 60)

# Top performer
top = max(performance, key=performance.get)

# Average score
avg = sum(performance.values()) / len(performance)

# Categories
excellent = [e for e, s in performance.items() if s >= 90]
good = [e for e, s in performance.items() if 75 <= s <= 89]
average = [e for e, s in performance.items() if 60 <= s <= 74]
poor = [e for e, s in performance.items() if s < 60]

# Output
print(above_80)
print(improve)
print(top, performance[top])
print(round(avg, 1))
print(excellent)
print(good)
print(average)
print(poor)