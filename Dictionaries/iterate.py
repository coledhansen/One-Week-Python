test_scores = {
    "Marsha": 78,
    "Baker": 69,
    "Rosa": 92,
    "Leif": 97,
    "Peng": 61,
    "Juan": 73,
    "Esteban": 84,
    "Amir": 91,
    "Sakura": 99 
}

# dict.keys()
# dict.values()
for student in test_scores.keys():
    print(student)
for score in test_scores.values():
    print(score)

total = 0
for score in test_scores.values():
    total += score
print(total/len(test_scores))

for key in test_scores.keys():
    print(key, test_scores[key])

# dict.items()
print(test_scores.items()) # both key and value

for item in test_scores.items():
    print(item) # tuple

max_score = 0
best_student = ""
for student, score in test_scores.items():
    if score > max_score:
        max_score = score
        best_student = student
print(f"Highest Score: {score} | Best Student: {student}")
