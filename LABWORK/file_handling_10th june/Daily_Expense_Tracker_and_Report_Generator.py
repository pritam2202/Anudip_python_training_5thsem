# Expense Tracker System

# Load expenses
def load():
    data = {}
    with open("expenses.txt", "r") as file:
        for line in file:
            c, a = line.strip().split(",")
            data[c] = int(a)
    return data


# Save expenses
def save(d):
    with open("expenses.txt", "w") as file:
        for k, v in d.items():
            file.write(f"{k},{v}\n")


# Generate report
def report(d):
    total = sum(d.values())
    high = max(d, key=d.get)
    low = min(d, key=d.get)

    with open("report.txt", "w") as file:
        file.write(f"Total: {total}\n")
        file.write(f"Highest: {high}\n")
        file.write(f"Lowest: {low}\n")
        file.write("Above 800:\n")

        for k, v in d.items():
            if v > 800:
                file.write(f"{k},{v}\n")

    print("Report Generated")


while True:
    data = load()

    print("\n1.Display 2.Total 3.High/Low 4.Above 800 5.Add 6.Update 7.Report 8.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print(data)

    elif ch == 2:
        print(sum(data.values()))

    elif ch == 3:
        print("High:", max(data, key=data.get))
        print("Low:", min(data, key=data.get))

    elif ch == 4:
        for k, v in data.items():
            if v > 800:
                print(k, v)

    elif ch == 5:
        data[input("Category: ")] = int(input("Amount: "))
        save(data)

    elif ch == 6:
        k = input("Category: ")
        if k in data:
            data[k] = int(input("New Amount: "))
            save(data)

    elif ch == 7:
        report(data)

    elif ch == 8:
        break
