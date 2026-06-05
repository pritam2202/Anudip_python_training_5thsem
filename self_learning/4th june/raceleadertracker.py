n = int(input("Enter number of racers: "))

lap_times = []

for i in range(n):
    time = float(input(f"Enter lap time of racer {i + 1}: "))
    lap_times.append(time)

fastest_time = min(lap_times)
slowest_time = max(lap_times)

fastest_pos = lap_times.index(fastest_time) + 1
slowest_pos = lap_times.index(slowest_time) + 1

difference = slowest_time - fastest_time

print("Fastest racer position:", fastest_pos)
print("Slowest racer position:", slowest_pos)
print("Difference:", difference)