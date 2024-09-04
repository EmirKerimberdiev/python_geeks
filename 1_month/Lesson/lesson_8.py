# Контекстный менеджер “with”, работа с файлами.
# w - write, re-write
# a - add
# x - проверяет файл на наличие, создаёт только новый файл
# r - read

# file = open('new_file.txt', 'w')
# file.write('Бишкек, Кыргызыстан!')
# file.close()


# with open('new_file.txt', 'a') as file:
#     file.write('\nтретяя строка')

# with open('new_file_1.txt', 'x') as file:
#     file.write('\nnew file')

from time import sleep
with open('new_file.txt', 'r') as file:

    for letter in file.readline().split():
        sleep(1)
        print(letter, end=" ")


