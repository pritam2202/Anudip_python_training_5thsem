
license_key = "ABCD-EFGH-IJKL-MNOP"

# 1. Create a list containing all groups
groups = license_key.split('-')

# Verify number of groups
group_count = len(groups)

# 2. Verify each group contains exactly 4 characters
valid_groups = True
for group in groups:
    if len(group) != 4:
        valid_groups = False
        break

# 3. Count total letters
merged_key = license_key.replace('-', '')
total_letters = len(merged_key)

# 4. Count vowels
vowels = "AEIOUaeiou"
vowel_count = 0

for ch in merged_key:
    if ch in vowels:
        vowel_count += 1

# 5. Remove hyphens and display merged key
# (already stored in merged_key)

# 7. Check license key validity
if group_count == 4 and valid_groups:
    status = "Valid"
else:
    status = "Invalid"

# Display Results
print("License Key:")
print(license_key)

print("\nGroups:")
print(groups)

print("\nNumber of Groups:", group_count)

print("\nTotal Letters:", total_letters)
print("Total Vowels:", vowel_count)

print("\nMerged Key:")
print(merged_key)

print("\nLicense Key Status:", status)