student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

def grading_system(name,score):
    if 90<score and score<=100:
        student_grades[name] = "Outstanding"
    elif 80<score and score<=90:
        student_grades[name] = "Exceeds Expection" 
    elif 70<score and score<=80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"  

for key in student_scores:
    grading_system(key,student_scores[key])
    
print(student_grades)                   