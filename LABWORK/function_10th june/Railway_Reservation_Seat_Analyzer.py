# Railway Reservation Seat Analyzer

seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# Function 1
def count_seats(seats):
    booked = seats.count("Booked")
    available = seats.count("Available")
    return booked, available

# Function 2
def first_available(seats):
    for i in range(len(seats)):
        if seats[i] == "Available":
            return i + 1      # Seat numbers start from 1
    return None

# Function 3
def occupancy_percentage(seats):
    booked = seats.count("Booked")
    return (booked / len(seats)) * 100

# Function 4
def display_available_seats(seats):
    print("Available Seat Numbers:")
    for i in range(len(seats)):
        if seats[i] == "Available":
            print(i + 1, end=" ")
    print()

# Main Program
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

print("\nFirst Available Seat:", first_available(seats))

print("\nOccupancy Percentage: {:.2f}%".format(
    occupancy_percentage(seats)))

display_available_seats(seats)
