# Delivery times in minutes
delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Find the fastest delivery time
fastest = min(delivery_times)
print("Fastest Delivery:", fastest, "minutes")

# 2. Find the slowest delivery time
slowest = max(delivery_times)
print("\nSlowest Delivery:", slowest, "minutes")

# 3. Calculate the average delivery time
average = sum(delivery_times) / len(delivery_times)
print("\nAverage Delivery Time:", round(average, 1), "minutes")

# 4. Display delayed orders (>45 minutes)
delayed_orders = [time for time in delivery_times if time > 45]
print("\nDelayed Orders:")
print(delayed_orders)

# 5. Categorize deliveries
fast_deliveries = [time for time in delivery_times if time <= 30]
normal_deliveries = [time for time in delivery_times if 31 <= time <= 45]
delayed_deliveries = [time for time in delivery_times if time > 45]

print("\nFast Deliveries:", len(fast_deliveries))
print("Normal Deliveries:", len(normal_deliveries))
print("Delayed Deliveries:", len(delayed_deliveries))
