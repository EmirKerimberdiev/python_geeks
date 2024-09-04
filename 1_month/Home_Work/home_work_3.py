sum = 0
consonants_ru = ["Б", "В", "Г", "Д", "Ж", "З", "Й", "К", "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ"]
con_ru = 0
vowels_ru = ["А", "И", "О", "У", "Ы", "Э"]
vow_ru = 0

consonants_en = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
con_en = 0
vowels_en = ["A", "E", "I", "O", "U"]
vow_en = 0

while True:
    word = str(input('Если хотите выйти и закончить программу то напишите "break".\nВведите любое слово на Кирилице или на Латинице: '))

    if word == "break":
        break

    for letter in word:
        sum += 1
        for row in consonants_ru:
            if letter.upper() == row:
                con_ru += 1
        for row1 in vowels_ru:
            if letter.upper() == row1:
                vow_ru += 1
        for row2 in consonants_en:
            if letter.upper() == row2:
                con_en += 1
        for row3 in vowels_en:
            if letter.upper() == row3:
                vow_en += 1

    sum_con = con_en + con_ru
    sum_vow = vow_ru + vow_en

    percent_con = sum_con / sum * 100
    percent_vow = sum_vow / sum * 100

    print('Слово:', word)
    print('Количество букв:', sum)
    print('Согластных букв',sum_con)
    print('Гласных букв', sum_vow)
    print(f'Гласные/Согласные: {round(percent_con, 2)}% / {round(percent_vow, 2)}%\n')

# mas = ["H", "L"]
# for row in mas:
#     print(row)
#     if row == "H":
#         print("YES")
#     else:
#         print("NO")




