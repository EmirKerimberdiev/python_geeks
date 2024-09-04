# Lambda функции. Обработка исключений.

# try:
#     print(2 * 'Hello')
# except:
#     print('!Ошибка найденна!')
# else:
#     print('Ок')
# finally:
#     print('Проверка завершенна')
#
# days = 1
# data = {}
# while days <=7:
#     print(data)
#     try:
#         data[days] = int(input(f'enter expense for day #{days}: '))
#     except:
#         print('введите только числа!')
#         continue
#     days += 1
#
# print(sum(data.values()))
# print(sum(data.values() / len(data)))


# lambda_func = lambda num1, num2: num1 + num2
# print(lambda_func)

names = ('akel', 'emir', 'dastan', 'lilya')
print(names)
mapped_names = list(map(lambda name: name.upper(), names))
print(mapped_names)
filter_names = list(filter(lambda name: 'm' in name, names))
print(filter_names)
sorted_names = sorted(names, key=lambda name: name[1])
print(sorted_names)


# def up_first_letter(word: str):
#     return word.title()
#
# def show_words(func, objects):
#     for i in objects:
#         print(func(i))
#
#
# show_words(up_first_letter, names)


# def get_square(length: int, width: int) -> int:
#     """
#     Принимает ширину и длинну, возвращает площядь.
#     """
#     return length * width
#
# print(help(get_square))
# print(get_square.__doc__)

# word: str = "Bishkek"
# cities = ['Tokmok', 'Karakol', 'Kant']
#
#
# def len1(objects: int) -> int:
#     counter = 0
#     for i in objects:
#         counter += 1
#     return counter

# print(len1(word))
# print(len1(cities))

# print(len(word))
# print(len(cities))
