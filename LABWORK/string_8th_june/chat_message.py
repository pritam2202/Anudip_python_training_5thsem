message = "Python is awesome and Python is easy to learn"

# 1. Count total characters (excluding spaces)
total_characters = len(message.replace(" ", ""))

# Split message into words
words = message.split()

# 2. Count total words
total_words = len(words)

# 3. Find the longest word
longest_word = max(words, key=len)

# 4. Find the shortest word
shortest_word = min(words, key=len)

# 5. Count occurrences of "Python"
python_count = words.count("Python")

# 6. List words having more than 4 characters
long_words = [word for word in words if len(word) > 4]

# 7. Display all words starting with a vowel
vowels = "AEIOUaeiou"
vowel_words = [word for word in words if word[0] in vowels]

# 8. Count vowels and consonants
vowel_count = 0
consonant_count = 0

for ch in message:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Display results
print("Message:")
print(message)

print("\nTotal Characters:", total_characters)
print("Total Words:", total_words)

print("\nLongest Word:", longest_word)
print("Shortest Word:", shortest_word)

print("\nOccurrences of Python:", python_count)

print("\nWords Longer Than 4 Characters:")
print(long_words)

print("\nWords Starting With a Vowel:")
print(vowel_words)

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)
