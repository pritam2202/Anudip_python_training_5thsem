# ==========================================
# CITY POPULATION & DEVELOPMENT DASHBOARD
# ==========================================

# 30 CITY RECORDS
cities = {
    "Delhi": {"population": 32000000, "area": 1484, "literacy": 89},
    "Mumbai": {"population": 21000000, "area": 603, "literacy": 92},
    "Bangalore": {"population": 14000000, "area": 709, "literacy": 94},
    "Chennai": {"population": 12000000, "area": 426, "literacy": 90},
    "Kolkata": {"population": 15000000, "area": 185, "literacy": 87},
    "Hyderabad": {"population": 10000000, "area": 650, "literacy": 83},
    "Pune": {"population": 7000000, "area": 331, "literacy": 91},
    "Jaipur": {"population": 4000000, "area": 467, "literacy": 85},
    "Lucknow": {"population": 3000000, "area": 631, "literacy": 82},
    "Surat": {"population": 6000000, "area": 326, "literacy": 89},
    "Goa": {"population": 1500000, "area": 3702, "literacy": 93},
    "Chandigarh": {"population": 1200000, "area": 114, "literacy": 95},
    "Mysore": {"population": 1100000, "area": 152, "literacy": 92},
    "Agra": {"population": 1600000, "area": 188, "literacy": 80},
    "Varanasi": {"population": 1400000, "area": 82, "literacy": 84},
    "Indore": {"population": 2200000, "area": 530, "literacy": 89},
    "Bhopal": {"population": 1900000, "area": 463, "literacy": 88},
    "Patna": {"population": 2000000, "area": 250, "literacy": 79},
    "Nagpur": {"population": 2400000, "area": 393, "literacy": 90},
    "Dehradun": {"population": 900000, "area": 196, "literacy": 94},
    "Shimla": {"population": 800000, "area": 35, "literacy": 93},
    "Guwahati": {"population": 1100000, "area": 216, "literacy": 91},
    "Amritsar": {"population": 1200000, "area": 139, "literacy": 87},
    "Ludhiana": {"population": 1800000, "area": 159, "literacy": 88},
    "Rajkot": {"population": 1300000, "area": 170, "literacy": 85},
    "Jodhpur": {"population": 1200000, "area": 233, "literacy": 83},
    "Udaipur": {"population": 1000000, "area": 64, "literacy": 90},
    "Kanpur": {"population": 2900000, "area": 403, "literacy": 81},
    "Vizag": {"population": 1700000, "area": 681, "literacy": 86},
    "Patiala": {"population": 900000, "area": 155, "literacy": 88}
}

# ------------------------------------------
# 1. DISPLAY ALL CITIES
# ------------------------------------------
def display_all():
    print("\n--- CITY DETAILS ---")
    for c in cities:
        print(c, cities[c])

# ------------------------------------------
# 2. MOST POPULATED CITY
# ------------------------------------------
def max_population():
    max_city = None
    for c in cities:
        if max_city is None or cities[c]["population"] > cities[max_city]["population"]:
            max_city = c
    print("Most Populated:", max_city, cities[max_city])

# ------------------------------------------
# 3. LEAST POPULATED CITY
# ------------------------------------------
def min_population():
    min_city = None
    for c in cities:
        if min_city is None or cities[c]["population"] < cities[min_city]["population"]:
            min_city = c
    print("Least Populated:", min_city, cities[min_city])

# ------------------------------------------
# 4. AVERAGE POPULATION
# ------------------------------------------
def avg_population():
    total = 0
    for c in cities:
        total += cities[c]["population"]
    avg = total / len(cities)
    print("Average Population:", avg)
    return avg

# ------------------------------------------
# 5. LITERACY > 90%
# ------------------------------------------
def high_literacy():
    print("\nHigh Literacy Cities (>90%):")
    for c in cities:
        if cities[c]["literacy"] > 90:
            print(c, cities[c])

# ------------------------------------------
# 6. LITERACY BELOW AVERAGE
# ------------------------------------------
def low_literacy():
    avg = 0
    for c in cities:
        avg += cities[c]["literacy"]
    avg = avg / len(cities)

    print("\nCities Below Average Literacy:")
    for c in cities:
        if cities[c]["literacy"] < avg:
            print(c, cities[c])

# ------------------------------------------
# 7. POPULATION DENSITY
# ------------------------------------------
def density(city):
    return cities[city]["population"] / cities[city]["area"]

# ------------------------------------------
# 8. HIGHEST DENSITY CITY
# ------------------------------------------
def max_density():
    top = None
    for c in cities:
        if top is None or density(c) > density(top):
            top = c
    print("Highest Density:", top, density(top))

# ------------------------------------------
# 9. CATEGORIZE CITIES
# ------------------------------------------
def categorize():
    print("\nCity Categories:")
    for c in cities:
        pop = cities[c]["population"]
        if pop < 1000000:
            print(c, "Small")
        elif pop < 5000000:
            print(c, "Medium")
        else:
            print(c, "Large")

# ------------------------------------------
# 10. DEVELOPMENT PRIORITY
# ------------------------------------------
def development_priority():
    print("\nDevelopment Priority (Low literacy first):")
    for c in cities:
        if cities[c]["literacy"] < 85:
            print(c, cities[c])

# ------------------------------------------
# 11. HIGH & LOW LITERACY DICTIONARIES
# ------------------------------------------
def literacy_groups():
    high = {}
    low = {}

    for c in cities:
        if cities[c]["literacy"] >= 90:
            high[c] = cities[c]
        else:
            low[c] = cities[c]

    print("\nHigh Literacy Cities:", high)
    print("\nLow Literacy Cities:", low)

# ------------------------------------------
# 12. NATIONAL REPORT
# ------------------------------------------
def report():
    total_pop = 0
    for c in cities:
        total_pop += cities[c]["population"]

    print("\n===== NATIONAL REPORT =====")
    print("Total Cities:", len(cities))
    print("Total Population:", total_pop)
    print("Average Population:", total_pop / len(cities))

# ------------------------------------------
# RANKING (NO SORT FUNCTION)
# ------------------------------------------
def ranking_density():
    temp = cities.copy()
    print("\nRanking by Density:")

    for _ in range(len(temp)):
        top = None
        for c in temp:
            if top is None or density(c) > density(top):
                top = c
        print(top, density(top))
        del temp[top]

# ------------------------------------------
# MENU
# ------------------------------------------
while True:
    print("\n===== CITY MENU =====")
    print("1. Display All Cities")
    print("2. Most Populated")
    print("3. Least Populated")
    print("4. Average Population")
    print("5. High Literacy (>90%)")
    print("6. Low Literacy")
    print("7. Highest Density")
    print("8. Categorize Cities")
    print("9. Development Priority")
    print("10. Literacy Groups")
    print("11. National Report")
    print("12. Density Ranking")
    print("13. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        display_all()
    elif ch == 2:
        max_population()
    elif ch == 3:
        min_population()
    elif ch == 4:
        avg_population()
    elif ch == 5:
        high_literacy()
    elif ch == 6:
        low_literacy()
    elif ch == 7:
        max_density()
    elif ch == 8:
        categorize()
    elif ch == 9:
        development_priority()
    elif ch == 10:
        literacy_groups()
    elif ch == 11:
        report()
    elif ch == 12:
        ranking_density()
    elif ch == 13:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
