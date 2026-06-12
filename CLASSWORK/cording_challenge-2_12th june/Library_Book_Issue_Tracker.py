# List of book issue counts
book_issues = [15, 8, 22, 10, 18, 5, 30, 12, 20, 25]

# Maximum issues
print(max(book_issues))

# Minimum issues
print(min(book_issues))

# Average issues
print(sum(book_issues) / len(book_issues))

# Count books issued more than 15 times
more_15 = sum(1 for x in book_issues if x > 15)

# Books issued fewer than 10 times
less_10 = [x for x in book_issues if x < 10]

print(more_15)
print(less_10)