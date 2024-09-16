def grade(x):
    if x >= 80:
        print('A')
    elif x >= 60:
        print('B')
    elif x >= 50:
        print('C')
    else:
        print('Fail')


score = int(input('What score did you get? : '))
if 0 <= score and score <= 100:
    grade(score)
else:
    print('Invalid Range')    