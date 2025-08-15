name = []
age = []

while True:
    choose = int(input('Add item list (1)\
        Exit(2)'))

    if choose == 2:
        break
    elif choose == 1:
        name_type = input("Type the name:")
        age_type = input('Type the age:')
        name.append(name_type)
        age.append(age_type)
        continue
    else:
        print("This option doenst exist!")
        continue

i = 0

for number in name:
    print(name[i],age[i])
    i += 1


