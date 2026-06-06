units = {
    "House101": 320,
    "House102": 180,
    "House103": 450,
    "House104": 290,
    "House105": 150,
    "House106": 510,
    "House107": 220,
    "House108": 390,
    "House109": 170,
    "House110": 260
}

# Houses consuming more than 300 units
print("Houses consuming more than 300 units:")
for house, unit in units.items():
    if unit > 300:
        print(house)

# Count houses consuming less than 200 units
count = 0
for unit in units.values():
    if unit < 200:
        count += 1
print("Houses consuming less than 200 units:", count)

# House with highest consumption
highest = max(units, key=units.get)
print("Highest consumption:", highest, "-", units[highest])

# Houses for awareness campaign
campaign = []
for house, unit in units.items():
    if unit > 400:
        campaign.append(house)
print("Awareness campaign houses:", campaign)

# Categorize houses
print("\nConsumption Category:")
for house, unit in units.items():

    if unit < 200:
        category = "Low"

    elif unit <= 350:
        category = "Medium"

    else:
        category = "High"

    print(house, ":", category)