# Library Book Management System

# Load books from file
def load_books():
    books = []
    with open("books.txt", "r") as file:
        for line in file:
            bid, name, qty = line.strip().split(",")
            books.append([bid, name, int(qty)])
    return books


# Save books to file
def save_books(books):
    with open("books.txt", "w") as file:
        for b in books:
            file.write(f"{b[0]},{b[1]},{b[2]}\n")


# Display books
def display(books):
    for b in books:
        print(b)


# Issue book (decrease quantity)
def issue(books):
    bid = input("Enter Book ID: ")
    for b in books:
        if b[0] == bid:
            if b[2] > 0:
                b[2] -= 1
                save_books(books)
                print("Book Issued")
            else:
                print("Not Available")
            return


# Return book (increase quantity)
def return_book(books):
    bid = input("Enter Book ID: ")
    for b in books:
        if b[0] == bid:
            b[2] += 1
            save_books(books)
            print("Book Returned")
            return


while True:
    books = load_books()

    print("\n1.Display 2.Issue 3.Return 4.Unavailable 5.Restock 6.Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        display(books)

    elif ch == 2:
        issue(books)

    elif ch == 3:
        return_book(books)

    elif ch == 4:
        for b in books:
            if b[2] == 0:
                print(b)

    elif ch == 5:
        for b in books:
            if b[2] < 2:
                print(b)

    elif ch == 6:
        break
