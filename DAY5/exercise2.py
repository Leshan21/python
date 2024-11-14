students_scores = input("Enter students scores: ")

list = students_scores.split(" ")

max_score = 0

for number in range(0, len(list)):
    if int(list[number]) > max_score:
        max_score = int(list[number])

print(f"The highest score in the calass is: {max_score}")        