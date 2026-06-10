# Movie Review Sentiment Analyzer

reviews = [
    "excellent movie",
    "average story",
    "excellent acting",
    "poor direction",
    "excellent visuals",
    "poor screenplay",
    "good music",
    "excellent climax",
    "average performance",
    "good cinematography"
]

# Function 1
def count_sentiments(reviews):
    excellent = good = average = poor = 0

    for review in reviews:
        if "excellent" in review:
            excellent += 1
        elif "good" in review:
            good += 1
        elif "average" in review:
            average += 1
        elif "poor" in review:
            poor += 1

    return excellent, good, average, poor

# Function 2
def most_common_word(reviews):
    words = []

    for review in reviews:
        words.extend(review.split())

    max_count = 0
    common_word = ""

    for word in set(words):
        count = words.count(word)
        if count > max_count:
            max_count = count
            common_word = word

    return common_word

# Function 3
def longest_review(reviews):
    return max(reviews, key=len)

# Function 4
def reviews_with_keyword(reviews, keyword):
    print(f"Reviews containing '{keyword}':")
    for review in reviews:
        if keyword.lower() in review.lower():
            print(review)

# Main Program
excellent, good, average, poor = count_sentiments(reviews)

print("Excellent Reviews:", excellent)
print("Good Reviews:", good)
print("Average Reviews:", average)
print("Poor Reviews:", poor)

print("\nMost Common Word:")
print(most_common_word(reviews))

print("\nLongest Review:")
print(longest_review(reviews))

print()
reviews_with_keyword(reviews, "excellent")
