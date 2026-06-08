
review = "This product is excellent excellent excellent and very useful"

# Split review into words
words = review.split()

# 1. Count total words
total_words = len(words)

# 2. Create a dictionary containing word frequencies
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# 3. Find the most frequently used word
most_frequent_word = max(word_freq, key=word_freq.get)

# 4. Find all words appearing only once
appearing_once = [word for word, count in word_freq.items() if count == 1]

# 5. Count words having more than 5 characters
more_than_5 = [word for word in words if len(word) > 5]
count_more_than_5 = len(more_than_5)

# 6. Display words in reverse order
reverse_words = words[::-1]

# 7. Create a list of unique words
unique_words = list(word_freq.keys())

# Display results
print("Total Words:", total_words)

print("\nWord Frequencies:")
for word, count in word_freq.items():
    print(word, "->", count)

print("\nMost Frequent Word:", most_frequent_word)

print("\nWords Appearing Once:")
print(appearing_once)

print("\nWords Having More Than 5 Characters:")
print(more_than_5)
print("Count:", count_more_than_5)

print("\nWords in Reverse Order:")
print(reverse_words)

print("\nUnique Words:")
print(unique_words)