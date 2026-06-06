# E-Commerce Order Analysis
#Problem Statement
#An online store records orders as:
#orders = [
 #("Laptop", 55000),
 #("Mouse", 800),
 #("Keyboard", 1500),
 #("Monitor", 12000),
 #("Pen Drive", 600)]
#Write a program to:
# Display all products costing more than ₹1000.
#Find the most expensive product.
#Calculate the total order value.
#Count products costing below ₹1000. 

# E-Commerce Order Analysis

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# Display products costing more than ₹1000
print("Products costing more than ₹1000:")
for product, price in orders:
    if price > 1000:
        print(product, "-", price)

# Find the most expensive product
max_product = orders[0][0]
max_price = orders[0][1]

for product, price in orders:
    if price > max_price:
        max_price = price
        max_product = product

print("\nMost Expensive Product:", max_product, "-", max_price)

# Calculate total order value
total = 0
for product, price in orders:
    total += price

print("Total Order Value: ₹", total)

# Count products costing below ₹1000
count = 0
for product, price in orders:
    if price < 1000:
        count += 1

print("Number of products costing below ₹1000:", count)
