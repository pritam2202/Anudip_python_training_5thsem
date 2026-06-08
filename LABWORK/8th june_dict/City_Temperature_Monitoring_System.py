# Dictionary storing city temperatures
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}

# Display cities above 40°C
print("Cities Above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# Find hottest and coolest city
hot = max(temperature, key=temperature.get)
cool = min(temperature, key=temperature.get)

print("\nHottest City:", hot, f"({temperature[hot]}°C)")
print("Coolest City:", cool, f"({temperature[cool]}°C)")

# Calculate average temperature
avg = sum(temperature.values()) / len(temperature)
print("\nAverage Temperature:", round(avg, 1), "°C")

# List pleasant cities
pleasant = [city for city, temp in temperature.items() if temp < 35]
print("\nPleasant Cities:")
print(pleasant)

# Count cities with temperatures between 35°C and 40°C
count = sum(1 for temp in temperature.values() if 35 <= temp <= 40)
print("\nCities Between 35°C and 40°C:", count)
