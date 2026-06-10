# Contact Management System

# Load contacts
def load():
    contacts = {}
    with open("contacts.txt", "r") as file:
        for line in file:
            name, num = line.strip().split(",")
            contacts[name] = num
    return contacts


# Save contacts
def save(c):
    with open("contacts.txt", "w") as file:
        for k, v in c.items():
            file.write(f"{k},{v}\n")


while True:
    contacts = load()

    print("\n1.Display 2.Search 3.Add 4.Update 5.Delete 6.Vowel Names 7.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        print(contacts)

    elif ch == 2:
        print(contacts.get(input("Name: "), "Not Found"))

    elif ch == 3:
        contacts[input("Name: ")] = input("Number: ")
        save(contacts)

    elif ch == 4:
        n = input("Name: ")
        if n in contacts:
            contacts[n] = input("New Number: ")
            save(contacts)

    elif ch == 5:
        n = input("Name: ")
        if n in contacts:
            del contacts[n]
            save(contacts)

    elif ch == 6:
        for k in contacts:
            if k[0].lower() in "aeiou":
                print(k, contacts[k])

    elif ch == 7:
        break
