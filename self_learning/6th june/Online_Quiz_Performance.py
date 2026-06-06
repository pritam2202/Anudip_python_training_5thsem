quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Students scoring 15 or above
print("Students scoring 15 or above:")
for student, score in quiz_scores.items():
    if score >= 15:
        print(student)

# Count below 10
count = 0
for score in quiz_scores.values():
    if score < 10:
        count += 1
print("Students below 10:", count)

# Top performer
top = max(quiz_scores, key=quiz_scores.get)
print("Top performer:", top)

# Passed students
passed = []
for student, score in quiz_scores.items():
    if score >= 10:
        passed.append(student)
print("Passed students:", passed)

# Class average
average = sum(quiz_scores.values()) / len(quiz_scores)
print("Class average:", average)