"""1-задание"""

# ближайшее число

def nearest_number(nums, target: int):
    sorted_nums = sorted(nums, key=lambda x: abs(x - target))
    return (target, sorted_nums)

numbers = []
while True:
    input_numbers = input('Введите числа сколько хотите. Для выхода введите "q": ')
    if input_numbers == 'q':
        break
    else:
        numbers.append(int(input_numbers))

target_number = int(input("Напишите целевое число: "))
result = nearest_number(numbers, target_number)
print("Целевое число и отсортированный список по приближенности:", result)



"""2-задание"""

# Как перевести градусы Цельсия в Фаренгейта?
# Если предполагается обратный перевод °C в°F,
# сначала нужно произвести умножение на девятку и поделить на пять,
# после чего увеличить результат на тридцать два градуса.
# Произведя пересчет 25°C по шкале Фаренгейта, получим следующее 25*9/5+32 = 77°F.

# def calculator_F(num: int):
#     return ((num * 9) / 5) + 32
#
# numbers = []
#
# while True:
#     input_numbers = input('Напишите числа которые хотите перевести в цельции. Для выхода введите "q": ')
#     if input_numbers == 'q':
#         break
#     else:
#         num = int(input_numbers)
#         result = calculator_F(num)
#         numbers.append(result)
#
# print(numbers)

"""3-задание"""


def access_element(iterable):
    while True:
        try:
            index = int(input(f"Введите индекс (от 0 до {len(iterable) - 1}).  Если хотите выйти введите 'q': "))
            if index == 'q':
                break
            print(f"Элемент по индексу {index}: {iterable[index]}\n")

        except IndexError:
            print(f"\nОшибка: индекс вне диапазона. Пожалуйста, введите индекс от 0 до {len(iterable) - 1}.\n")

my_tuple = ('emir', 'nurahim', 'tilek', 'mucadas')
print("\nРаботаем с кортежем:")
access_element(my_tuple)

