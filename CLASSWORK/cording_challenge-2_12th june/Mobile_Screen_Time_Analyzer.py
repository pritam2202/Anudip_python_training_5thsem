# Daily screen time data (in minutes)
screen_time = [180, 220, 150, 300, 120, 250, 190, 210, 175, 260]

# 1. Calculate average screen time
average_time = sum(screen_time) / len(screen_time)
print("Average Screen Time:", round(average_time, 1), "minutes")

# 2. Find the highest and lowest screen time
highest_time = max(screen_time)
lowest_time = min(screen_time)

print("\nHighest Screen Time:", highest_time, "minutes")
print("Lowest Screen Time:", lowest_time, "minutes")

# 3. Count days exceeding 200 minutes
days_exceeding_200 = sum(1 for time in screen_time if time > 200)
print("\nDays Exceeding 200 Minutes:", days_exceeding_200)

# 4. Display days with healthy usage (<180 minutes)
print("\nHealthy Usage Days:")
for day, time in enumerate(screen_time, start=1):
    if time < 180:
        print(f"Day {day}")

# 5. Categorize usage
healthy = sum(1 for time in screen_time if time < 180)
moderate = sum(1 for time in screen_time if 180 <= time <= 240)
excessive = sum(1 for time in screen_time if time > 240)

print("\nHealthy:", healthy)
print("Moderate:", moderate)
print("Excessive:", excessive)
