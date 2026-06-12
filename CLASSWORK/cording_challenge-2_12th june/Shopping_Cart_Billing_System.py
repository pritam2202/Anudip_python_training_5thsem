# Tuple of product prices
prices = (1250, 799, 450, 999, 300, 1500, 650, 250, 850, 1200)

# Total bill
print(sum(prices))

# Most expensive product
print(max(prices))

# Least expensive product
print(min(prices))

# Count products above 1000
above_1000 = sum(1 for p in prices if p > 1000)

# Discount eligible products (>800)
discount = [p for p in prices if p > 800]

print(above_1000)
print(discount)