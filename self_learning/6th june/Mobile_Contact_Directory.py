contacts = {
    "Amit": "9876543210",
    "Priya": "9876543211",
    "Rohan": "9876543212",
    "Neha": "9876543213",
    "Anjali": "9876543214",
    "Karan": "9876543215",
    "Pooja": "9876543216",
    "Arjun": "9876543217",
    "Sneha": "9876543218",
    "Rahul": "9876543219"
}

# Display contacts alphabetically
print("Contacts in alphabetical order:")
for name in sorted(contacts):
    print(name)

# Total contacts
print("Total contacts:", len(contacts))

# Search for a contact
search_name = input("Enter contact name: ")

for name, number in contacts.items():
    if name == search_name:
        print("Contact Found:", number)
        break
else:
    print("Contact Not Found")

# Names starting with vowels
vowel_contacts = []
for name in contacts:
    if name[0].lower() in "aeiou":
        vowel_contacts.append(name)

print("Names starting with vowels:", vowel_contacts)