f= open("data.txt", "r")

data = f.read()

vowels = 0
characters = 0

for ch in data:
    if ch.lower() in "aeiou":
        vowels += 1

    if ch != " " and ch != "\n":
        characters += 1

lines = data.count("\n") + 1

print("No. of Vowels =", vowels)
print("No. of Characters =", characters)
print("No. of Lines =", lines)

f.close()