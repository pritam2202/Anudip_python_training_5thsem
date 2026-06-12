# Open feedback file in read mode
file = open("feedback.txt", "r")

# Read all lines
lines = file.readlines()

# Count total lines
total_lines = len(lines)

# Split all words
words = " ".join(lines).split()

# Count total words
total_words = len(words)

# Count total characters
total_chars = sum(len(line) for line in lines)

# Find longest feedback line
longest = max(lines, key=len).strip()

# Find shortest feedback line
shortest = min(lines, key=len).strip()

# Count vowels
vowels = "aeiouAEIOU"
vowel_count = sum(1 for c in "".join(lines) if c in vowels)

# Print results
print(total_lines)
print(total_words)
print(total_chars)
print(longest)
print(shortest)
print(vowel_count)

file.close()