#10. Train Reservation Waiting List
#Problem Statement
#Passenger records:
#passengers = [
# ("Anuj", "Confirmed"),
# ("Rahul", "Waiting"),
# ("Priya", "Confirmed"),
# ("Amit", "Waiting"),
# ("Neha", "Confirmed")
#]
#Write a program to:
#• Display all waiting-list passengers.
#• Count confirmed and waiting passengers.
#• Find whether a specific passenger has a confirmed ticket.
#• Create separate lists for confirmed and waiting passengers.



passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

confirmed = 0
waiting = 0

confirmed_list = []
waiting_list = []

print("Waiting List Passengers:")

for name, status in passengers:
    if status == "Waiting":
        print(name)

for name, status in passengers:
    if status == "Confirmed":
        confirmed += 1
        confirmed_list.append(name)
    else:
        waiting += 1
        waiting_list.append(name)

print("Confirmed:", confirmed)
print("Waiting:", waiting)

search = input("Enter passenger name: ")

found = False

for name, status in passengers:
    if name == search and status == "Confirmed":
        found = True
        break

if found:
    print("Confirmed Ticket")
else:
    print("Not Confirmed")

print("Confirmed List:", confirmed_list)
print("Waiting List:", waiting_list)
