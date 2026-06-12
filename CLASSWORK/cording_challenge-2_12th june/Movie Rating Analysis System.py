ratings = {
    "Inception": 4.8,
    "Avatar": 4.3,
    "Titanic": 4.5,
    "Joker": 4.7,
    "Frozen": 3.8,
    "Interstellar": 4.9,
    "Dune": 4.6,
    "Up": 4.1,
    "Coco": 4.4,
    "Cars": 3.9
}

above_4_5 = [m for m, r in ratings.items() if r > 4.5]

best = max(ratings, key=ratings.get)
worst = min(ratings, key=ratings.get)
avg = sum(ratings.values()) / len(ratings)
recommended = [m for m, r in ratings.items() if r >= 4.5]

print("Movies Rated Above 4.5:", above_4_5)
print("Highest Rated:", best, ratings[best])
print("Lowest Rated:", worst, ratings[worst])
print("Average Rating:", round(avg, 1))
print("Recommended:", recommended)