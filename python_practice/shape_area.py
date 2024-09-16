def equation(r_t):
    global answer
    if r_t == 'triangle' or r_t == 't':
        answer=1/2*base*height
    elif r_t == 'rectangle' or r_t == 'r':
        answer=base*height


base=float(input('What is the width of your shape? (Metres) : '))
height=float(input('What is the height of your shape? (Metres) : '))
r_t=input('Do you want to calculate the area of a triangle (t) or rectangle (r)? : ')
equation(r_t)
print(f'The area of your shape is {answer}m')
