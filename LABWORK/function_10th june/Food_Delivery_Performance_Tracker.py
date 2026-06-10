# Food Delivery Performance Tracker

delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# Function 1
def fastest_delivery(times):
    return min(times)

# Function 2
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    return delayed

# Function 3
def average_delivery_time(times):
    return sum(times) / len(times)

# Function 4
def delivery_category(times):
    print("Categories:")
    for t in times:
        if t <= 30:
            category = "Fast"
        elif t <= 45:
            category = "Normal"
        else:
            category = "Delayed"

        print(t, "->", category)

# Main Program
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

print("\nAverage Delivery Time:")
print(round(average_delivery_time(delivery_time), 1), "minutes")

print()
delivery_category(delivery_time)
