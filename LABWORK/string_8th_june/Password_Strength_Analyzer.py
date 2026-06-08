# Password Strength Analyzer

# Input password
password = input("Enter Password: ")

# Counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0

# Lists to store digits and special characters
digits_found = []
special_found = []

# Check each character
for ch in password:

    if ch.isupper():
        upper_count += 1

    elif ch.islower():
        lower_count += 1

    elif ch.isdigit():
        digit_count += 1
        digits_found.append(ch)

    else:
        special_count += 1
        special_found.append(ch)

# Determine password strength
if (len(password) >= 8 and
    upper_count >= 1 and
    lower_count >= 1 and
    digit_count >= 1 and
    special_count >= 1):

    strength = "Strong"

elif len(password) >= 6 and (digit_count > 0 or special_count > 0):
    strength = "Medium"

else:
    strength = "Weak"

# Display results
print("\nPassword:", password)

print("\nUppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)
print("Digits:", digit_count)
print("Special Characters:", special_count)

print("\nDigits Found:", digits_found)
print("Special Characters Found:", special_found)

print("\nPassword Strength:", strength)
