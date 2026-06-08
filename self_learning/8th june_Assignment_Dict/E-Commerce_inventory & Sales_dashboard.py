# ==========================================
# E-COMMERCE INVENTORY & SALES DASHBOARD
# ==========================================

# 30 product records
products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Phone", "price": 20000, "stock": 5, "sold": 40},
    "P103": {"name": "Tablet", "price": 15000, "stock": 2, "sold": 10},
    "P104": {"name": "Mouse", "price": 500, "stock": 50, "sold": 100},
    "P105": {"name": "Keyboard", "price": 1000, "stock": 30, "sold": 80},
    "P106": {"name": "Monitor", "price": 12000, "stock": 0, "sold": 20},
    "P107": {"name": "Printer", "price": 8000, "stock": 3, "sold": 15},
    "P108": {"name": "Camera", "price": 30000, "stock": 7, "sold": 18},
    "P109": {"name": "Headphones", "price": 1500, "stock": 20, "sold": 60},
    "P110": {"name": "Speaker", "price": 2500, "stock": 8, "sold": 35},
    "P111": {"name": "TV", "price": 40000, "stock": 4, "sold": 22},
    "P112": {"name": "AC", "price": 35000, "stock": 6, "sold": 12},
    "P113": {"name": "Fan", "price": 2000, "stock": 25, "sold": 70},
    "P114": {"name": "Light", "price": 300, "stock": 60, "sold": 90},
    "P115": {"name": "Router", "price": 1800, "stock": 10, "sold": 45},
    "P116": {"name": "SSD", "price": 5000, "stock": 9, "sold": 55},
    "P117": {"name": "HDD", "price": 4000, "stock": 11, "sold": 30},
    "P118": {"name": "RAM", "price": 3500, "stock": 13, "sold": 65},
    "P119": {"name": "GPU", "price": 60000, "stock": 1, "sold": 5},
    "P120": {"name": "CPU", "price": 25000, "stock": 2, "sold": 8},
    "P121": {"name": "Charger", "price": 800, "stock": 15, "sold": 75},
    "P122": {"name": "Cable", "price": 200, "stock": 40, "sold": 120},
    "P123": {"name": "PowerBank", "price": 3000, "stock": 5, "sold": 50},
    "P124": {"name": "Projector", "price": 22000, "stock": 3, "sold": 14},
    "P125": {"name": "Mic", "price": 1200, "stock": 18, "sold": 33},
    "P126": {"name": "Tripod", "price": 900, "stock": 22, "sold": 27},
    "P127": {"name": "Drone", "price": 45000, "stock": 1, "sold": 6},
    "P128": {"name": "Scanner", "price": 7000, "stock": 4, "sold": 19},
    "P129": {"name": "HardDisk", "price": 6000, "stock": 6, "sold": 44},
    "P130": {"name": "SmartWatch", "price": 5000, "stock": 12, "sold": 58}
}

# ------------------------------------------
# 1. Display all products
# ------------------------------------------
def display_products():
    print("\n--- ALL PRODUCTS ---")
    for pid in products:
        print(pid, products[pid])

# ------------------------------------------
# 2. Add new product
# ------------------------------------------
def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    stock = int(input("Enter Stock: "))
    sold = int(input("Enter Sold: "))

    products[pid] = {
        "name": name,
        "price": price,
        "stock": stock,
        "sold": sold
    }

    print("Product Added")

# ------------------------------------------
# 3. Update stock after sales
# ------------------------------------------
def update_stock():
    pid = input("Enter Product ID: ")

    if pid in products:
        sold_qty = int(input("Enter quantity sold: "))
        products[pid]["stock"] -= sold_qty
        products[pid]["sold"] += sold_qty
        print("Stock Updated")
    else:
        print("Product not found")

# ------------------------------------------
# 4. Out of stock products
# ------------------------------------------
def out_of_stock():
    print("\n--- OUT OF STOCK ---")
    for pid in products:
        if products[pid]["stock"] == 0:
            print(pid, products[pid])

# ------------------------------------------
# 5. Low stock (<5)
# ------------------------------------------
def low_stock():
    print("\n--- LOW STOCK PRODUCTS ---")
    for pid in products:
        if products[pid]["stock"] < 5:
            print(pid, products[pid])

# ------------------------------------------
# 6. Total inventory value
# ------------------------------------------
def inventory_value():
    total = 0
    for pid in products:
        total += products[pid]["price"] * products[pid]["stock"]

    print("Total Inventory Value:", total)

# ------------------------------------------
# 7. Best selling product
# ------------------------------------------
def best_selling():
    best = None
    for pid in products:
        if best is None or products[pid]["sold"] > products[best]["sold"]:
            best = pid

    print("Best Selling:", best, products[best])

# ------------------------------------------
# 8. Least selling product
# ------------------------------------------
def least_selling():
    low = None
    for pid in products:
        if low is None or products[pid]["sold"] < products[low]["sold"]:
            low = pid

    print("Least Selling:", low, products[low])

# ------------------------------------------
# 9. Total revenue
# ------------------------------------------
def revenue():
    total = 0
    for pid in products:
        total += products[pid]["price"] * products[pid]["sold"]

    print("Total Revenue:", total)

# ------------------------------------------
# 10. Low stock report
# ------------------------------------------
def low_stock_report():
    report = {}
    for pid in products:
        if products[pid]["stock"] < 5:
            report[pid] = products[pid]

    print("\nLow Stock Report:", report)

# ------------------------------------------
# 11. Above average sales
# ------------------------------------------
def above_avg_sales():
    total = 0

    for pid in products:
        total += products[pid]["sold"]

    avg = total / len(products)

    print("\nProducts Above Average Sales:")
    for pid in products:
        if products[pid]["sold"] > avg:
            print(pid, products[pid])

# ------------------------------------------
# 12. Promotion products (sold < 10)
# ------------------------------------------
def promotion():
    promo = {}
    for pid in products:
        if products[pid]["sold"] < 10:
            promo[pid] = products[pid]

    print("\nPromotion Products:", promo)

# ------------------------------------------
# MENU SYSTEM
# ------------------------------------------
while True:
    print("\n===== E-COMMERCE MENU =====")
    print("1. Display Products")
    print("2. Add Product")
    print("3. Update Stock After Sale")
    print("4. Out of Stock Products")
    print("5. Low Stock Products")
    print("6. Inventory Value")
    print("7. Best Selling Product")
    print("8. Least Selling Product")
    print("9. Total Revenue")
    print("10. Low Stock Report")
    print("11. Above Average Sales")
    print("12. Promotion Products")
    print("13. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        display_products()
    elif choice == 2:
        add_product()
    elif choice == 3:
        update_stock()
    elif choice == 4:
        out_of_stock()
    elif choice == 5:
        low_stock()
    elif choice == 6:
        inventory_value()
    elif choice == 7:
        best_selling()
    elif choice == 8:
        least_selling()
    elif choice == 9:
        revenue()
    elif choice == 10:
        low_stock_report()
    elif choice == 11:
        above_avg_sales()
    elif choice == 12:
        promotion()
    elif choice == 13:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
