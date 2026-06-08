# ==========================================
# SMART LIBRARY MANAGEMENT SYSTEM
# ==========================================

# 30 BOOK RECORDS
library = {
    "B101": {"title": "Python Basics", "author": "ABC", "copies": 5},
    "B102": {"title": "Data Structures", "author": "John", "copies": 2},
    "B103": {"title": "AI Fundamentals", "author": "Smith", "copies": 0},
    "B104": {"title": "Machine Learning", "author": "David", "copies": 7},
    "B105": {"title": "DBMS", "author": "Lee", "copies": 3},
    "B106": {"title": "Operating Systems", "author": "Kim", "copies": 6},
    "B107": {"title": "Computer Networks", "author": "Brown", "copies": 1},
    "B108": {"title": "Java Programming", "author": "Steve", "copies": 4},
    "B109": {"title": "C Programming", "author": "Alex", "copies": 8},
    "B110": {"title": "Web Development", "author": "Mike", "copies": 2},
    "B111": {"title": "Cloud Computing", "author": "Sam", "copies": 5},
    "B112": {"title": "Cyber Security", "author": "Tom", "copies": 0},
    "B113": {"title": "Blockchain", "author": "Ravi", "copies": 6},
    "B114": {"title": "IoT Basics", "author": "Karan", "copies": 9},
    "B115": {"title": "Advanced Python", "author": "ABC", "copies": 3},
    "B116": {"title": "HTML CSS", "author": "John", "copies": 10},
    "B117": {"title": "DSA Advanced", "author": "Alex", "copies": 2},
    "B118": {"title": "SQL Complete", "author": "Kim", "copies": 4},
    "B119": {"title": "Linux Guide", "author": "Lee", "copies": 5},
    "B120": {"title": "Big Data", "author": "Smith", "copies": 1},
    "B121": {"title": "Robotics", "author": "Brown", "copies": 6},
    "B122": {"title": "Deep Learning", "author": "David", "copies": 7},
    "B123": {"title": "Theory of Computation", "author": "Steve", "copies": 2},
    "B124": {"title": "Computer Graphics", "author": "Mike", "copies": 3},
    "B125": {"title": "Mathematics", "author": "Ravi", "copies": 8},
    "B126": {"title": "Physics", "author": "Sam", "copies": 9},
    "B127": {"title": "Chemistry", "author": "Tom", "copies": 4},
    "B128": {"title": "Biology", "author": "Alex", "copies": 5},
    "B129": {"title": "English", "author": "John", "copies": 2},
    "B130": {"title": "Hindi Literature", "author": "ABC", "copies": 6}
}

# ==========================================
# 1. ADD BOOK
# ==========================================
def add_book():
    bid = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    copies = int(input("Enter Copies: "))

    library[bid] = {"title": title, "author": author, "copies": copies}
    print("Book Added Successfully")

# ==========================================
# 2. REMOVE BOOK
# ==========================================
def remove_book():
    bid = input("Enter Book ID: ")
    if bid in library:
        del library[bid]
        print("Book Removed")
    else:
        print("Book Not Found")

# ==========================================
# 3. SEARCH BY ID
# ==========================================
def search_id():
    bid = input("Enter Book ID: ")
    if bid in library:
        print(library[bid])
    else:
        print("Book Not Found")

# ==========================================
# 4. SEARCH BY TITLE
# ==========================================
def search_title():
    name = input("Enter Title: ")
    found = False

    for bid in library:
        if library[bid]["title"].lower() == name.lower():
            print(bid, library[bid])
            found = True

    if not found:
        print("Not Found")

# ==========================================
# 5. UPDATE COPIES
# ==========================================
def update_copies():
    bid = input("Enter Book ID: ")
    if bid in library:
        copies = int(input("Enter New Copies: "))
        library[bid]["copies"] = copies
        print("Updated")
    else:
        print("Book Not Found")

# ==========================================
# 6. ISSUE BOOK
# ==========================================
def issue_book():
    bid = input("Enter Book ID: ")
    if bid in library:
        if library[bid]["copies"] > 0:
            library[bid]["copies"] -= 1
            print("Book Issued")
        else:
            print("Book Unavailable")
    else:
        print("Book Not Found")

# ==========================================
# 7. RETURN BOOK
# ==========================================
def return_book():
    bid = input("Enter Book ID: ")
    if bid in library:
        library[bid]["copies"] += 1
        print("Book Returned")
    else:
        print("Book Not Found")

# ==========================================
# 8. LESS THAN 3 COPIES
# ==========================================
def low_copies():
    print("\nBooks with <3 Copies:")
    for bid in library:
        if library[bid]["copies"] < 3:
            print(bid, library[bid])

# ==========================================
# 9. UNAVAILABLE BOOKS
# ==========================================
def unavailable():
    print("\nUnavailable Books:")
    for bid in library:
        if library[bid]["copies"] == 0:
            print(bid, library[bid])

# ==========================================
# 10. MOST AVAILABLE BOOK
# ==========================================
def most_available():
    max_book = None

    for bid in library:
        if max_book is None or library[bid]["copies"] > library[max_book]["copies"]:
            max_book = bid

    print("Most Available:", max_book, library[max_book])

# ==========================================
# 11. RESTOCK REPORT
# ==========================================
def restock_report():
    report = {}

    for bid in library:
        if library[bid]["copies"] < 3:
            report[bid] = library[bid]

    print("\nRestocking Report:", report)

# ==========================================
# 12. IMMEDIATE PURCHASE
# ==========================================
def immediate_purchase():
    urgent = {}

    for bid in library:
        if library[bid]["copies"] == 0:
            urgent[bid] = library[bid]

    print("\nImmediate Purchase List:", urgent)

# ==========================================
# MAIN MENU
# ==========================================
while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search by ID")
    print("4. Search by Title")
    print("5. Update Copies")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Low Copies (<3)")
    print("9. Unavailable Books")
    print("10. Most Available Book")
    print("11. Restock Report")
    print("12. Immediate Purchase List")
    print("13. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_book()
    elif choice == 2:
        remove_book()
    elif choice == 3:
        search_id()
    elif choice == 4:
        search_title()
    elif choice == 5:
        update_copies()
    elif choice == 6:
        issue_book()
    elif choice == 7:
        return_book()
    elif choice == 8:
        low_copies()
    elif choice == 9:
        unavailable()
    elif choice == 10:
        most_available()
    elif choice == 11:
        restock_report()
    elif choice == 12:
        immediate_purchase()
    elif choice == 13:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
