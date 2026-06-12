# Inventory data
inventory = {
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

# 1. Display products with stock below 15 units
print("Products with Stock Below 15:")
for product, stock in inventory.items():
    if stock < 15:
        print(product)

# 2. Find the product with maximum stock
max_product = max(inventory, key=inventory.get)
print("\nHighest Stock Product:")
print(f"{max_product} ({inventory[max_product]} units)")

# 3. Find the product with minimum stock
min_product = min(inventory, key=inventory.get)
print("\nLowest Stock Product:")
print(f"{min_product} ({inventory[min_product]} units)")

# 4. Calculate total stock available
total_stock = sum(inventory.values())
print("\nTotal Stock Available:", total_stock)

# 5. Create a list of products requiring restocking (<10 units)
restocking = [product for product, stock in inventory.items() if stock < 10]

print("\nProducts Requiring Restocking:")
print(restocking)
