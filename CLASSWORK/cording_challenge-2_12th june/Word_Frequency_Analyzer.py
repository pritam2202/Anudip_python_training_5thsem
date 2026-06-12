# Open article file
file = open("article.txt", "r")

# Read and split words
words = file.read().lower().split()

# Frequency dictionary
freq = {}

# Count word frequency
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Most frequent word
most = max(freq, key=freq.get)

# Words appearing once
once = [w for w, c in freq.items() if c == 1]

# Output
print(len(words))
print(most, freq[most])
print(once)
print(len(freq))
