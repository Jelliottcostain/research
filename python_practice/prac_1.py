import random

name = "Anna"
my_age = 32
height = 1.76
married=False
print(f'Their name is {name}. They are {my_age} Years old. And have a height of {height} metres.')

gender=bool(random.randint(0,1))
if gender:
    print('its male')
else:
    print('its female')