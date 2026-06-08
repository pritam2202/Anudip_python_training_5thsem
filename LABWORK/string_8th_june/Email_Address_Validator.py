
email = "rahul.sharma2026@gmail.com"

# 1. Extract username
username = email.split("@")[0]

# 2. Extract domain name
domain = email.split("@")[1].split(".")[0]

# 3. Extract extension
extension = email.split(".")[-1]

# 4. Count digits present in username
digit_count = 0
for ch in username:
    if ch.isdigit():
        digit_count += 1

# 5. Count special characters
special_count = 0
for ch in email:
    if not ch.isalnum():
        special_count += 1

# 6. Validate email
at_count = email.count("@")

if at_count == 1:
    domain_part = email.split("@")[1]
    valid = "." in domain_part
else:
    valid = False

# 7. Display results
print("Email:", email)

print("\nUsername:", username)
print("Domain:", domain)
print("Extension:", extension)

print("\nDigits Found:", digit_count)
print("Special Characters Found:", special_count)

if valid:
    print("\nValid Email")
else:
    print("\nInvalid Email")