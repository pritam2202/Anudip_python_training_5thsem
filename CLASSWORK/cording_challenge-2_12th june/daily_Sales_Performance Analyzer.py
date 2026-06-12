# Sales data for 10 days
sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

# Calculate average sales
avg = sum(sales) / len(sales)

# Highest sales
print(max(sales))

# Lowest sales
print(min(sales))

# Average sales
print(avg)

# Count days above 20k
above = sum(1 for s in sales if s > 20000)

# Sales below average
below_avg = [s for s in sales if s < avg]

print(above)
print(below_avg)
