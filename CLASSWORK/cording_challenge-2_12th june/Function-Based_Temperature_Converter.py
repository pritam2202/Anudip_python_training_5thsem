# List of temperatures in Celsius
temps = [25, 30, 35, 40, 28, 32, 38, 22, 27, 31]

# Function to convert Celsius to Fahrenheit
def c_to_f(c):
    return (c * 9/5) + 32

# Convert all temperatures
f_temps = [c_to_f(t) for t in temps]

# Highest Fahrenheit temperature
print(max(f_temps))

# Lowest Fahrenheit temperature
print(min(f_temps))

# Average Fahrenheit temperature
print(sum(f_temps)/len(f_temps))

# Print all converted temperatures
print(f_temps)