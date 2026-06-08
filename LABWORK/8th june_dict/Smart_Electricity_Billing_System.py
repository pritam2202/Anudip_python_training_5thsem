# Dictionary storing electricity consumption
units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}

# Display houses consuming more than 400 units
print("Houses Consuming More Than 400 Units:")
for house, unit in units.items():
    if unit > 400:
        print(house)

# Find highest and lowest consumption
highest = max(units, key=units.get)
lowest = min(units, key=units.get)

print("\nHighest Consumption:")
print(highest, f"({units[highest]} units)")

print("\nLowest Consumption:")
print(lowest, f"({units[lowest]} units)")

# Calculate total units consumed
print("\nTotal Units Consumed:", sum(units.values()))

# Categorize houses by consumption
low = [house for house, unit in units.items() if unit < 200]
medium = [house for house, unit in units.items() if 200 <= unit <= 400]
high = [house for house, unit in units.items() if unit > 400]

print("\nLow Consumption:")
print(low)

print("\nMedium Consumption:")
print(medium)

print("\nHigh Consumption:")
print(high)

# Count houses eligible for energy-saving campaign
campaign = sum(1 for unit in units.values() if unit > 300)
print("\nEligible for Energy-Saving Campaign:", campaign)
