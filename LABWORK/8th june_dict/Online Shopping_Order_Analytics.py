# Dictionary storing product sales
sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, qty in sales.items():
    if qty > 20:
        print(product)

# Find best-selling and least-selling products
best = max(sales, key=sales.get)
least = min(sales, key=sales.get)

print("\nBest Selling Product:", best, f"({sales[best]})")
print("Least Selling Product:", least, f"({sales[least]})")

# Calculate total units sold
print("\nTotal Units Sold:", sum(sales.values()))

# Create list of products requiring promotion
promotion = [product for product, qty in sales.items() if qty < 15]
print("\nProducts Requiring Promotion:")
print(promotion)

# Count products with sales between 10 and 30
count = sum(1 for qty in sales.values() if 10 <= qty <= 30)
print("\nProducts Having Sales Between 10 and 30:", count)
