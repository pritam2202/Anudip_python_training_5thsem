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

# 1. Cities with temperature above 40°C
above_40 = [city for city, temp in temperature.items() if temp > 40]

# 2. Hottest city
hottest_city = max(temperature, key=temperature.get)

# 3. Coolest city
coolest_city = min(temperature, key=temperature.get)

# 4. Average temperature
average_temp = sum(temperature.values()) / len(temperature)

# 5. Pleasant cities (<35°C)
pleasant_cities = [city for city, temp in temperature.items() if temp < 35]

# Display results
print("Cities Above 40°C:")
for city in above_40:
    print(city)

print("\nHottest City:")
print(f"{hottest_city} ({temperature[hottest_city]}°C)")

print("\nCoolest City:")
print(f"{coolest_city} ({temperature[coolest_city]}°C)")

print(f"\nAverage Temperature: {average_temp:.1f}°C")

print("\nPleasant Cities:")
print(pleasant_cities)
