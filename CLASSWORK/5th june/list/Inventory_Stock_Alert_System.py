stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Display products that are out of stock
print("Out of Stock Products:")
for i in range(len(stock)):
    if stock[i] == 0:
        print("Product", i + 1, "is out of stock")

# 2. Display products that need restocking (quantity less than 10)
print("\nProducts Needing Restocking:")
for i in range(len(stock)):
    if stock[i] < 10:
        print("Product", i + 1, "Stock:", stock[i])

# 3. Count available products
available_count = 0
for qty in stock:
    if qty > 0:
        available_count += 1

print("\nAvailable Products:", available_count)

# 4. Create a new list containing only products with stock >= 15
high_stock = []
for qty in stock:
    if qty >= 15:
        high_stock.append(qty)

print("Products with Stock >= 15:", high_stock)