# Number of copies available for each book
books = {
    "Python": 5,
    "Java": 2,
    "DBMS": 4,
    "Networking": 1,
    "OS": 3,
    "AI": 6,
    "ML": 2,
    "Cloud": 5,
    "Cyber Security": 1,
    "Web Development": 4
}

# 1. Display books with fewer than 3 copies
print("Books Requiring Attention:")
for book, copies in books.items():
    if copies < 3:
        print(book)

# 2. Find the book with maximum copies
max_book = max(books, key=books.get)
print("\nBook with Maximum Copies:")
print(f"{max_book} ({books[max_book]} copies)")

# 3. Find the book with minimum copies
min_book = min(books, key=books.get)
print("\nBook with Minimum Copies:")
print(f"{min_book} ({books[min_book]} copies)")

# 4. Count total books available
total_copies = sum(books.values())
print("\nTotal Copies Available:", total_copies)

# 5. Generate a restocking list
restocking_list = [book for book, copies in books.items() if copies < 3]

print("\nRestocking List:")
print(restocking_list)
