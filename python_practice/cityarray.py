city = []
for x in range(0,5):
    name = str(input('Name a city: '))
    city += [name]
print(len(city))
city += [str('Hong')]
city.pop(0)
city.reverse()
print(city)