def get_feetback():
    feedback = input('Введите "да", "больше" или "меньше": \n').lower()
    if feedback in "да" "больше" "меньше":
        return feedback
    else:
        print('Введите только "да", "больше" или "меньше"! ')

def get_num():
    low, high = 1, 100
    attempt = 0
    guesses = []

    while True:
        gues = (low + high) // 2
        attempt += 1
        guesses.append(gues)

        print("Я думаю что это", gues)
        feedback = get_feetback()

        if feedback == "да":
            with open('new_file.txt', 'w') as file:
                file.write(f'Количество попыток: {attempt}\n')
                file.write(f'Список попыток: {guesses}\n')
                file.write(f'Загаданное число: {gues}\n')
                print(f'Рядом с этим файлом создалсы ещё один файл с названием "new_file.txt"')
                break

        elif feedback == "больше":
            low = gues + 1
        elif feedback == "меньше":
            high = gues - 1

print(get_num())