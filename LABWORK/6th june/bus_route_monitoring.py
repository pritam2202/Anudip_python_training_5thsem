#8. Bus Route Monitoring
#Problem Statement
#Passenger count at each stop:
#passengers = [12, 18, 25, 30, 28, 15, 8]
#Write a program to:
#• Find the busiest stop.
#• Display stops with fewer than 10 passengers.
#• Calculate average passengers.
#• Determine whether any stop exceeded 25 passengers. 


passengers = [12, 18, 25, 30, 28, 15, 8]

highest = passengers[0]
position = 1
total = 0
exceeded = False

for i in range(len(passengers)):
    total += passengers[i]

    if passengers[i] > highest:
        highest = passengers[i]
        position = i + 1

    if passengers[i] > 25:
        exceeded = True

print("Busiest Stop:", position)

print("Stops with less than 10 passengers:")
for i in range(len(passengers)):
    if passengers[i] < 10:
        print(i + 1)

average = total / len(passengers)

print("Average Passengers:", average)

if exceeded:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")
