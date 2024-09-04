mentors = ["Тимур", "Арсен", "Гулина",  "Даниель"]
sum = 0
sensor = 0
while True:
    options = int(input('-------Выберите опцию-------\n1 - Добавить нового ментора\n2 - Поменять ментора\n3 - Удалить ментора\n0 - Выход\n'))
    print(mentors)

# Добавление
    if options == 1:
        name = input("Поожалуйста введите имя ментора что бы добавить его в список: ")
        for letter in name:
            sum += 1
        for row in mentors:
            if row == name.title():
                print("\nПростите этот ментор уже есть в списке. Добавте другого ментора (например Эмира)\n")
                sensor = 1
        if len(mentors) > 9:
            print("\nКоличество менторов привысила 10 человек!!!\n")
        elif sum > 15:
            print("\nКоличество символов в имени привысило 15!!!\n")
        elif sensor == 0:
            mentors.append(name.title())
            print("\n", mentors)
        sum = 0
        continue

# Изменение
    elif options == 2:
        name_old = input("Поожалуйста введите имя ментора которого хотите заменить: ").title().strip()

        if name_old not in mentors:
            print("\nЭтого ментора нельзя заменит поскольку его нет в списке!\n")
            continue

        name_new = str(input("Поожалуйста введите имя ментора которого хотите добавить: "))

        for letter in name_new:
            sum += 1
        if len(mentors) > 9:
            print("\nКоличество менторов привысила 10 человек!!!\n")
        elif sum > 15:
            print("\nКоличество символов в имени привысило 15!!!\n")
        else:
            index = mentors.index(name_old)
            mentors[index] = name_new.title()
        print("\n", mentors)
        sum = 0
        continue

# Удаление
    elif options == 3:
        delete = int(input("Как вы хотите удалить ментора\n1 - Удалить по имени\n2 - Удалить по индексу\n"))
        if delete == 1:
            name = input("Введите имя ментора которого хотите удалить: ")
            mentors.remove(name.title())
            print(mentors)
        elif delete == 2:
            name = int(input("Введите индекс ментора которого хотите удалить: "))
            mentors.pop(name)
            print("\n", mentors)
        continue

# Выход
    else:
        mentors = tuple
        print("\n", mentors)
        break