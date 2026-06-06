books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Unavailable books
print("Unavailable books:")
for book, copies in books.items():
    if copies == 0:
        print(book)

# Count available books
available = 0
for copies in books.values():
    if copies > 0:
        available += 1
print("Available books:", available)

# Book with maximum copies
maximum = max(books, key=books.get)
print("Book with maximum copies:", maximum)

# Books with less than 3 copies
few_copies = []
for book, copies in books.items():
    if copies < 3:
        few_copies.append(book)
print("Books with less than 3 copies:", few_copies)

# Total books available
total = sum(books.values())
print("Total books available:", total)