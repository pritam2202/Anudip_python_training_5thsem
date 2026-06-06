#Books available in a library:
#books = [
# ("Python Basics", 5),
# ("Data Science", 0),
# ("Java Programming", 3),
 #("Machine Learning", 0)
#]
#Write a program to:
#• Display unavailable books.
#• Find all books with more than 2 copies.
#• Count available books.
#• Stop searching once a requested book is found. 

books = [
    ("Python Basics", 5),
    ("Data Science", 0),
    ("Java Programming", 3),
    ("Machine Learning", 0)
]

available = 0

print("Unavailable Books:")
for book, copies in books:
    if copies == 0:
        print(book)

print("Books with more than 2 copies:")
for book, copies in books:
    if copies > 2:
        print(book)

for book, copies in books:
    if copies > 0:
        available += 1

print("Available Books:", available)

search = input("Enter book name: ")

for book, copies in books:
    if book == search:
        print("Book Found")
        break
