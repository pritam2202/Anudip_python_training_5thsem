class RailwayReservationSystem:
    def __init__(self):
        self.passengers = {}
        self.tickets = {}

    def register_passenger(self):
        name = input("Enter passenger name: ")
        age = int(input("Enter age: "))
        self.passengers[name] = age
        print("Passenger registered successfully.")

    def book_ticket(self):
        pnr = input("Enter PNR number: ")
        name = input("Enter passenger name: ")
        source = input("Enter source station: ")
        destination = input("Enter destination station: ")
        self.tickets[pnr] = {
            "name": name,
            "source": source,
            "destination": destination,
            "status": "Booked"
        }
        print("Ticket booked successfully.")

    def cancel_ticket(self):
        pnr = input("Enter PNR number: ")
        if pnr in self.tickets:
            self.tickets[pnr]["status"] = "Cancelled"
            print("Ticket cancelled successfully.")
        else:
            print("PNR not found.")

    def search_ticket(self):
        pnr = input("Enter PNR number: ")
        if pnr in self.tickets:
            print(self.tickets[pnr])
        else:
            print("Ticket not found.")

    def pnr_status(self):
        pnr = input("Enter PNR number: ")
        if pnr in self.tickets:
            print("PNR Status:", self.tickets[pnr]["status"])
        else:
            print("PNR not found.")

    def reports(self):
        print("\nAll Tickets")
        for pnr, details in self.tickets.items():
            print("PNR:", pnr, details)


system = RailwayReservationSystem()

while True:
    print("\n--- Railway Reservation System ---")
    print("1. Passenger Registration")
    print("2. Ticket Booking")
    print("3. Ticket Cancellation")
    print("4. Search Ticket")
    print("5. PNR Status")
    print("6. Reports")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        system.register_passenger()
    elif choice == "2":
        system.book_ticket()
    elif choice == "3":
        system.cancel_ticket()
    elif choice == "4":
        system.search_ticket()
    elif choice == "5":
        system.pnr_status()
    elif choice == "6":
        system.reports()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
