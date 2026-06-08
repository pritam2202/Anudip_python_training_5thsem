
text = "AAABBBCCCDDDAAA"

# Frequency Dictionary
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Character Frequencies:")
for k, v in freq.items():
    print(k, "->", v)

# Unique Characters
print("\nUnique Characters:")
print(list(freq.keys()))

# Most Frequent Character
most_freq = max(freq, key=freq.get)
print("\nMost Frequent Character:", most_freq)

# Compression
compressed = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        compressed += text[i - 1] + str(count)
        count = 1

compressed += text[-1] + str(count)

print("\nCompressed Output:", compressed)

# Compression Ratio
original_len = len(text)
compressed_len = len(compressed)

ratio = (compressed_len / original_len) * 100

print("\nOriginal Length:", original_len)
print("Compressed Length:", compressed_len)
print("Compression Ratio: {:.2f}%".format(ratio))