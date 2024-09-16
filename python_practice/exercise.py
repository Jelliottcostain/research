# Name and Age arrays
name_list = []
age_list = []

# While loop for collecting and creating records
key = 'y'
while key == 'y':
    name = str(input("Enter a name: "))
    age = int(input("Enter an age: "))
    # Asks user if they want to keep adding more records
    key = input("Do you wish to add another record (y/n): ")
    name_list += [name]
    age_list += [age]

# Prints basic results of both lists
print(name_list)
print(age_list)

# Prints out lists in x, y format.
for x in range(len(name_list)):
    print(f"{name_list[x]}, {age_list[x]}")

# Prints out all ages until it finds an age less than 20 then it STOPS
# While loop
a = 20
count = 0
while a >= 20:
    print(age_list[count])
    a = age_list[count]
    count += 1
# For loop
for y in age_list:
    print(y)
    if y < 20:
        break
# Prints out all ages except under 20
for z in age_list:
    if z >= 20:
        print(z)
    else:
        print()

count = 0
a = 20
while count < len(age_list):
    a = age_list[count]
    if a >= 20:
        print(age_list[count])
    else:
        print()
    count += 1

    