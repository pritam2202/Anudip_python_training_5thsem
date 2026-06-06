#7. Online Quiz Evaluation
#Problem Statement
#Correct answers:
#correct = ['A', 'C', 'B', 'D', 'A']
#Student answers:
#student = ['A', 'B', 'B', 'D', 'C']
#Write a program to:
#• Calculate score.
#• Display incorrectly answered question numbers.
#• Count correct and wrong answers.
#• Determine pass/fail (minimum 60%). 



correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
wrong = 0

for i in range(len(correct)):
    if correct[i] == student[i]:
        score += 1
    else:
        wrong += 1

print("Incorrect Question Numbers:")

for i in range(len(correct)):
    if correct[i] != student[i]:
        print(i + 1)

percentage = (score / len(correct)) * 100

print("Score:", score)
print("Correct:", score)
print("Wrong:", wrong)

if percentage >= 60:
    print("Pass")
else:
    print("Fail")
