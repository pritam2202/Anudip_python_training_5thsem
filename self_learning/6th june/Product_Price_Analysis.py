prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Products costing more than 5000
print("Products costing more than 5000:")
for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

# Count products less than 3000
count = 0
for price in prices.values():
    if price < 3000:
        count += 1
print("Products costing less than 3000:", count)

# Most expensive product
expensive = max(prices, key=prices.get)
print("Most expensive product:", expensive)

# Products priced between 2000 and 10000
products = []
for product, price in prices.items():
    if 2000 <= price <= 10000:
        products.append(product)
print("Products priced between 2000 and 10000:", products)

# Total value of products
total_value = sum(prices.values())
print("Total value:", total_value)