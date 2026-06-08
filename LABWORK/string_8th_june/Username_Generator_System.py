
name = "Rahul Sharma"

# 1. Remove spaces
username = name.replace(" ", "")

# 2. Convert to lowercase
username = username.lower()

# 3. Append current year (2026)
username = username + "2026"

# Username before trimming
original_username = username

# 4. If username length exceeds 12, keep only first 12 characters
if len(username) > 12:
    username = username[:12]

# 5 & 6. Count vowels and consonants
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for ch in original_username:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# 7. Display username statistics
print("Original Name:", name)

print("\nGenerated Username:")
print(original_username)

print("\nUsername Length:", len(original_username))

print("\nVowels:", vowel_count)
print("Consonants:", consonant_count)

print("\nStatus: Username Generated Successfully")