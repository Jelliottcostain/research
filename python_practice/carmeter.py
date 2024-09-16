

print('Kia Ora, this is a parking meter')
parkTime=int(input('How many hours will you be parking for? '))
rate=0
cost=0
while parkTime > 0:
    if parkTime <= 3:
        rate = 4
    else:
        rate = 2
    cost += rate
    parkTime -= 1
print(f'Your total is ${cost}')