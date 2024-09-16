def grading(x):
    global grade
    if x >= 80:
        grade = 'A'
    elif x >= 60:
        grade = 'B'
    elif x >= 50:
        grade = 'C'
    else:
        grade = 'Fail'
key = False
score = int(input("What is your score: "))
while key == False:  
    if 0 <= score and score <= 100:
        grading(score)
        print(grade)
        key = True
    else:
        score = int(input("Please enter a score between 0 and 100: "))