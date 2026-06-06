passengers = {
    "Stop1": 12,
    "Stop2": 25,
    "Stop3": 18,
    "Stop4": 32,
    "Stop5": 9,
    "Stop6": 28,
    "Stop7": 14,
    "Stop8": 7,
    "Stop9": 21,
    "Stop10": 16
}

# Stops with more than 20 passengers
print("Stops with more than 20 passengers:")
for stop, count in passengers.items():
    if count > 20:
        print(stop)

# Stops with fewer than 10 passengers
less_than_10 = 0
for count in passengers.values():
    if count < 10:
        less_than_10 += 1
print("Stops with fewer than 10 passengers:", less_than_10)

# Busiest stop
busiest = max(passengers, key=passengers.get)
print("Busiest stop:", busiest)

# Stops requiring extra bus
extra_bus = []
for stop, count in passengers.items():
    if count > 25:
        extra_bus.append(stop)
print("Extra bus required:", extra_bus)

# Average passengers
average = sum(passengers.values()) / len(passengers)
print("Average passengers:", average)