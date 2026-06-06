#Problem Statement
#A batsman's scores in different matches are stored in a list.
#scores = [45, 78, 12, 100, 67, 8, 90, 55]
#Write a program to:
#• Count half-centuries and centuries.
#• Find the highest score.
#• Display all scores below 20.
#• Calculate the average score. 


scores = [45, 78, 12, 100, 67, 8, 90, 55]

half = 0
century = 0
highest = scores[0]
total = 0

for score in scores:
    total += score

    if score >= 50 and score < 100:
        half += 1

    if score >= 100:
        century += 1

    if score > highest:
        highest = score

print("Scores below 20:")
for score in scores:
    if score < 20:
        print(score)

average = total / len(scores)

print("Half Centuries:", half)
print("Centuries:", century)
print("Highest Score:", highest)
print("Average:", average)
