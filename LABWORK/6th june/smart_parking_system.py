#Problem Statement
#Parking slots are represented as:
#slots = [1, 0, 1, 1, 0, 0, 1, 0]
#Where:
#• 1 = Occupied
#• 0 = Available
#Write a program to:
#• Count occupied and available slots.
#• Find the first available slot.
#• Display all available slot numbers.
#• Check whether parking occupancy exceeds 75%. 


slots = [1, 0, 1, 1, 0, 0, 1, 0]

occupied = 0
available = 0

for slot in slots:
    if slot == 1:
        occupied += 1
    else:
        available += 1

print("Occupied:", occupied)
print("Available:", available)

for i in range(len(slots)):
    if slots[i] == 0:
        print("First Available Slot:", i + 1)
        break

print("Available Slot Numbers:")
for i in range(len(slots)):
    if slots[i] == 0:
        print(i + 1)

occupancy = (occupied / len(slots)) * 100

if occupancy > 75:
    print("Occupancy exceeds 75%")
else:
    print("Occupancy does not exceed 75%")
