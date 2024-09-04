# Операторы: принадлежности, назначения * Циклы

# number = 5
#
# """операторы назначения"""
#
# number += 10
# number -= 3
# number **= 2
# number //= 2
#
# print(number)


"""операторы принадлежности - in"""

# word = "geeks"
# print("g" in word)
# print("i" in word)
# print(3 in 10)
# print(5 in range(1, 11))
# print(25 in range(1, 11))


"""Циклы"""

# rounds = 0
#
# while rounds < 100:
#     rounds += 1
#     if rounds == 50:
#         print("exit")
#         break
#     if rounds % 2 == 0:
#         continue
#     print("GEEKS", rounds)


# attempts = int(input('how many rounds? '))
# while attempts > 0:
#     print(f'попыток осталось: {attempts}')
#     temperature = input('Введите температуру: ')
#     if temperature.lower() == "выход":
#         break
#     elif temperature.isnumeric():
#         temperature = int(temperature)
#         if -40 <= temperature <= 0:
#             print('ХОЛОДНО')
#         elif temperature >= 1 and temperature <= 15:
#             print('ПРОХЛАДНО')
#         elif temperature >= 16 and temperature <= 25:
#             print("ТЕПЛО")
#         elif temperature >= 26 and temperature <= 40:
#             print('XAPA')
#         else:
#             print(f"несовместимая с жизнью температурą {temperature} градусов!")
#         attempts -= 1
#     else:
#         print("Введите 'выход' правильно")

rates = 0
question = 0

while True:
    answer = input("Оценка за вопрос: ")
    if answer.lower() == "exit":
        break
    else:
        question += 1
        rates += answer
    print(f"вопросв: {question}\n"
          f"сумма оценок: {rates}"
          f"средний показатель: {rates / question}")