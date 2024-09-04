# # def get_film():
# #     for i in movies:
# #         print(f'{i}: {movies[i]}')
#
#
#
# movies = {
#     "Django Unchained": {
#         "John": 10,
#         "Jack": 9
#     },
#
#     "Troy": {}
# }
# sensor = 0
# sensor_1 = 0
# sensor_2 = 0
# while True:
#     options = int(input('-------Выберите опцию-------\n1 - Добавить фильм\n2 - Добавить рейтинг к фильму\n3 - Просмотреть рейтинги для всех фильмов\n0 - Выход\n'))
#
#
# # Добавление
#     if options == 1:
#         for i in movies:
#             print(f'{i}: {movies[i]}')
#         name_of_move = input("Поожалуйста введите названия фильма который хотите добавить: ")
#
#         for row in movies:
#             if row == name_of_move.title():
#                 print('\nПростите этот фильм уже есть в рейтингах. Добавьте другой фильм.(Например"Путь станавление Ментором")\n')
#                 sensor = 1
#
#         if sensor == 0:
#             movies[name_of_move.title()] = {}
#             for i in movies:
#                 print(f'{i}: {movies[i]}')
#             print("\nФильм добавлен.")
#
#
# # Рэйтинг
#     elif options == 2:
#         for i in movies:
#             print(f'{i}: {movies[i]}')
#         name_of_seurch = input("Поожалуйста введите фильм к которому вы хотите добавить рейтинг: ").title().strip()
#
#         for row in movies:
#             if row == name_of_seurch:
#                 sensor_2 = 1
#
#         if sensor_2 == 0:
#             print('\nПростите этого фильма нет в рейтингах.\n')
#
#         elif sensor_2 == 1:
#             name_of_user = input("Введите своё имя: ")
#             rating = int(input(f'Введите рейтинг для фильма "{name_of_seurch}": '))
#
#             for row in movies[name_of_seurch]:
#                 if name_of_user.title() == row:
#                     print("Это имя уже оставила свою реакцию. Выберите другое имя!\n")
#                     sensor_1 = 1
#
#
#             if 0 <= rating <= 10 and sensor_1 == 0:
#                 movies[name_of_seurch][name_of_user.title()] = rating
#                 print(f'\nРэйтинг был добавлен для фильма "{name_of_seurch}": {name_of_user.title()} райтинг {rating}\n')
#                 sensor = 0
#             elif 0 > rating > 10:
#                 print("Такого рэйтинга нет!")
#
#
# # Отчёт
#     elif options == 3:
#         for movie, ratings in movies.items():
#             if ratings:
#                 average_rating = sum(ratings.values()) / len(ratings)
#                 print(f'Рэйтинг фильма "{movie}" это {average_rating:.1f}')
#             else:
#                 print(f'Рэйтинг для фильма "{movie}" пока не доступен.')
#
# # Выход
#     elif options == 0:
#         print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣶⣶⣦⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣷⣤⠄⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⠆⠰⠶⠄⠘⢿⣿⣿⣿⣿⣿⣆⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿⣿⠏⠄⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀\n⠄⠄⠄⠄⠄⠄⠄⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠄⡻⣿⣿⣿⣿⡇\n⠄⠄⠄⠄⠄⢀⠜⠁⠸⣿⣿⣿⠟⠄⠄⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇\n⠄⠄⠄⠄⡰⠉⠖⣀⠄⠄⢁⣀⠄⣴⣶⣦⠄⢴⡆⠄⠄⢀⣀⣀⣉⡽⠷⠶⠋⠄\n⠄⠄⠄⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠄⠄⣐⣲⣤⣯⠞⠉⠁⠄⠄⠄⠄⠄\n⠄⢀⠔⠁⣿⣿⣿⣿⣿⡟⠄⠄⠄⢀⣄⣀⡞⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⡜⠄⠄⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⢰⠁⠄⡤⠖⠺⢶⡾⠃⠄⠈⠙⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠈⠓⠾⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
#         break
#
#
#
#

# Функция для добавления
def add_film(movies):
    sensor = 0
    for i in movies:
        print(f'{i}: {movies[i]}')
    name_of_move = input("Поожалуйста введите названия фильма который хотите добавить: ")

    for row in movies:
        if row == name_of_move.title():
            print('\nПростите этот фильм уже есть в рейтингах. Добавьте другой фильм.(Например"Путь станавление Ментором")\n')
            sensor = 1

    if sensor == 0:
        movies[name_of_move.title()] = {}
        for i in movies:
            print(f'{i}: {movies[i]}')
        print("\nФильм добавлен.")

# Функция рейтинг к фильму
def add_rating(movies):
    sensor_1 = 0
    sensor_2 = 0
    for i in movies:
        print(f'{i}: {movies[i]}')
    name_of_seurch = input("Поожалуйста введите фильм к которому вы хотите добавить рейтинг: ").title().strip()

    for row in movies:
        if row == name_of_seurch:
            sensor_2 = 1

    if sensor_2 == 0:
        print('\nПростите этого фильма нет в рейтингах.\n')

    elif sensor_2 == 1:
        name_of_user = input("Введите своё имя: ")
        rating = int(input(f'Введите рейтинг для фильма "{name_of_seurch}": '))

        for row in movies[name_of_seurch]:
            if name_of_user.title() == row:
                print("\nЭто имя уже оставила свою реакцию. Выберите другое имя!\n")
                sensor_1 = 1


        if 0 <= rating <= 10 and sensor_1 == 0:
            movies[name_of_seurch][name_of_user.title()] = rating
            print(f'\nРэйтинг был добавлен для фильма "{name_of_seurch}": {name_of_user.title()} райтинг {rating}\n')
            sensor = 0
        elif 0 > rating > 10:
            print("Такого рэйтинга нет!")

# Функция рейтинг
def view_ratings(movies):
    for movie, ratings in movies.items():
        if ratings:
            average_rating = sum(ratings.values()) / len(ratings)
            print(f'Рейтинг фильма "{movie}" это {average_rating:.1f}')
        else:
            print(f'Рейтинг для фильма "{movie}" пока не доступен.')

# Функция меню
def menu():
    movies = {
        "Django Unchained": {
            "John": 10,
            "Jack": 9
        },
        "Troy": {}
    }

    while True:
        options = int(input('-------Выберите опцию-------\n1 - Добавить фильм\n2 - Добавить рейтинг к фильму\n3 - Просмотреть рейтинги для всех фильмов\n0 - Выход\n'))

        if options == 1:
            add_film(movies)
        elif options == 2:
            add_rating(movies)
        elif options == 3:
            view_ratings(movies)
        elif options == 0:
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⣶⣶⣦⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢠⣷⣤⠄⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⠆⠰⠶⠄⠘⢿⣿⣿⣿⣿⣿⣆⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿⣿⠏⠄⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠄\n⠄⠄⠄⠄⠄⠄⠄⠄⢠⠋⢈⣉⠉⣡⣤⢰⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣷⡀\n⠄⠄⠄⠄⠄⠄⠄⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠄⡻⣿⣿⣿⣿⡇\n⠄⠄⠄⠄⠄⢀⠜⠁⠸⣿⣿⣿⠟⠄⠄⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇\n⠄⠄⠄⠄⡰⠉⠖⣀⠄⠄⢁⣀⠄⣴⣶⣦⠄⢴⡆⠄⠄⢀⣀⣀⣉⡽⠷⠶⠋⠄\n⠄⠄⠄⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠄⠄⣐⣲⣤⣯⠞⠉⠁⠄⠄⠄⠄⠄\n⠄⢀⠔⠁⣿⣿⣿⣿⣿⡟⠄⠄⠄⢀⣄⣀⡞⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⡜⠄⠄⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⢰⠁⠄⡤⠖⠺⢶⡾⠃⠄⠈⠙⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n⠈⠓⠾⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
            break
menu()